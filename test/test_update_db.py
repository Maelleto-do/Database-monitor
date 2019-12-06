#!/usr/bin/env python3.7

import sys
import os
import unittest
import pymysql
import logging
import datetime

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
        cur = cards_bd.db_execute(self.conn, "DESCRIBE players")
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
        update_card_db.add_player(
            self.conn, "pseudoJoueurTest", "nomJoueurTest", "prenomJoueurTest"
        )
        sql_req = "SELECT * FROM players"
        cur = cards_bd.db_execute(self.conn, sql_req)
        res = cur.fetchall()
        self.assertIn(
            {
                "pseudo": "pseudoJoueurTest",
                "player_name": "nomJoueurTest",
                "player_first_name": "prenomJoueurTest",
            },
            res,
        )

    def test_2_remove_player(self):
        update_card_db.remove_player(self.conn, "pseudoJoueurTest")
        sql_req = "SELECT * FROM players"
        cur = cards_bd.db_execute(self.conn, sql_req)
        self.assertNotIn({"pseudo": "pseudoJoueurTest"}, cur.fetchall())

    # def test_3_add_deck(self):
    #     update_card_db.add_deck(self.conn, nom_deck="Magie", pseudo="Merlin")

    # def test_3_remove_deck(self):
    #     update_card_db.remove_deck(self.conn, nom_deck="Magie")

    def test_4_add_card(self):
        update_card_db.add_card(self.conn, title="Le Roi")
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM cards")
        self.assertEqual(
            cur.fetchone()["title"], "Le Roi", "La carte n'est pas 'le Roi'"
        )

    def test_4_remove_card(self):
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM cards")
        carte_id = cur.fetchone()["id_card"]
        update_card_db.remove_card(self.conn, id_card=carte_id)
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM cards where id_card = 1")
        result = cur.fetchall()
        self.assertEqual(len(result), 0, "Card is not deleted : {}".format(result))

    def test_5_add_card_version(self):
        update_card_db.add_card(self.conn, title="Le Roi")
        cur = cards_bd.db_execute(
            self.conn, "SELECT * FROM cards where title = 'Le Roi'"
        )
        carte_id = cur.fetchone()["id_card"]
        update_card_db.add_card_version(
            self.conn, id_card=carte_id, rendering="Brillant"
        )
        cur = cards_bd.db_execute(
            self.conn, "SELECT * FROM versions where id_card = {}".format(carte_id)
        )
        self.assertEqual(
            cur.fetchone()["rendering"], "Brillant", "La version n'a pas été créée"
        )

    def test_5_remove_card_version(self):
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM versions")
        version_id = cur.fetchone()["id_version"]
        update_card_db.remove_card_version(self.conn, id_version=version_id)
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM versions")
        self.assertEqual(len(cur.fetchall()), 0)

    def test_6_add_possession(self):
        # Prerequisites
        update_card_db.add_card(self.conn, title="Le Roi soleil")
        cur = cards_bd.db_execute(
            self.conn, "SELECT * FROM cards where title = 'Le Roi soleil'"
        )
        update_card_db.add_player(self.conn, "PSEUDO", "NOM", "PRENOM")
        card_id = cur.fetchone()["id_card"]
        update_card_db.add_card_version(
            self.conn, id_card=card_id, rendering="Brillant"
        )
        cur = cards_bd.db_execute(
            self.conn, "SELECT * FROM versions where id_card = %s", card_id
        )
        id_version = cur.fetchone()["id_version"]
        # Parameters
        pseudo = "PSEUDO"
        # Test
        update_card_db.add_possession(self.conn, pseudo, id_version)
        cur = cards_bd.db_execute(
            self.conn, "SELECT * FROM possessions where pseudo = %s", (pseudo),
        )
        possession = cur.fetchone()

        self.assertEqual(possession["pseudo"], pseudo, "Le pseudo n'est pas le bon")
        self.assertEqual(
            possession["id_version"], id_version, "La version n'est pas la bonne"
        )

    def test_6_remove_possession(self):
        # Parameters
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM possessions")
        id_possession = cur.fetchone()["id_possession"]
        # Test
        update_card_db.remove_possession(self.conn, id_possession)
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM possessions")
        possessions = cur.fetchall()
        self.assertEqual(len(possessions), 0)

    def test_7_add_game(self):
        # Parameters
        game_date = "2018-09-24 22:21:20"
        game_location = "Paris"
        tournament_type = "Amateur"
        game_results = "PSEUDO"  # id of winner
        # Test
        update_card_db.add_game(
            self.conn, game_date, game_location, tournament_type, game_results
        )
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM games")
        game = cur.fetchone()
        self.assertEqual(
            game["game_date"], datetime.date(2018, 9, 24), "La date n'est pas la bonne"
        )
        self.assertEqual(
            game["game_location"], game_location, "Le lieu n'est pas le bon"
        )
        self.assertEqual(
            game["tournament_type"], tournament_type, "Le type n'est pas le bon"
        )
        self.assertEqual(
            game["game_results"], game_results, "Les résultats ne sont pas les bons"
        )

    def test_7_remove_game(self):
        # Parameters
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM games")
        id_game = cur.fetchone()["id_game"]
        # Test
        update_card_db.remove_game(self.conn, id_game)
        cur = cards_bd.db_execute(self.conn, "SELECT * FROM games")
        self.assertEqual(len(cur.fetchall()), 0, "La partie n'a pas été supprimée")

    def test_9_drop_db(self):
        update_card_db.drop_tables(self.conn)
        cur = cards_bd.db_execute(self.conn, "SHOW TABLES")
        assert (
            cur.fetchone() == None
        ), "There are still tables in the database after drop_db call"
