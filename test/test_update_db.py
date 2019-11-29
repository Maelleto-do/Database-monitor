#!/usr/bin/env python3.7

import sys
import os
import unittest
import pymysql
import logging

import cards_bd
import update_card_db

host = os.environ["DB_HOST"]
user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


class TestUpdate(unittest.TestCase):
    """Unit tests for the update request"""

    def __init__(self, *args, **kwargs):
        super(TestUpdate, self).__init__(*args, **kwargs)
        cards_bd.init()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db_name,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def test_1_create_db(self):
        update_card_db.create_tables(self.conn)
        cur = cards_bd.db_execute(self.conn, "DESCRIBE joueurs")
        self.assertEqual(
            cur.fetchone(),
            {
                "Field": "pseudo",
                "Type": "varchar(64)",
                "Null": "NO",
                "Key": "PRI",
                "Default": None,
                "Extra": "",
            },
            "Incorrect Initialisation",
        )

    def test_2_add_player(self):
        pass

    def test_2_remove_player(self):
        pass

    # def test_3_add_deck(self):
    #     update_card_db.add_deck(self.conn, nom_deck="Magie", pseudo="Merlin")

    # def test_3_remove_deck(self):
    #     update_card_db.remove_deck(self.conn, nom_deck="Magie")

    def test_4_add_card(self):
        update_card_db.add_card(self.conn, title="Le Roi")
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM cartes")
        self.assertEqual(
            cur.fetchone()["titre"], "Le Roi", "La carte n'est pas 'le Roi'"
        )

    def test_4_remove_card(self):
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM cartes")
        carte_id = cur.fetchone()["id_carte"]
        update_card_db.remove_card(self.conn, id_card=carte_id)

    def test_5_add_card_version(self):
        pass

    def test_5_remove_card_version(self):
        pass

    def test_6_add_possession(self):
        pass

    def test_6_remove_possession(self):
        pass

    def test_7_add_game(self):
        pass

    def test_7_remove_game(self):
        pass

    def test_9_drop_db(self):
        update_card_db.drop_tables(self.conn)
        cur = cards_bd.db_execute(self.conn, "SHOW TABLES")
        assert (
            cur.fetchone() == None
        ), "There are still tables in the database after drop_db call"
