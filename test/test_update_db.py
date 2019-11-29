#!/usr/bin/env python3.7

import sys
import os
import unittest
import pymysql

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

    def test_create_db(self):
        pass

    def test_drop_db(self):
        pass

    def test_add_player(self):
        pass

    def test_remove_player(self):
        pass

    def test_add_deck(self):
        pass

    def test_remove_deck(self):
        pass

    def test_add_card(self):
        pass

    def test_remove_card(self):
        pass

    def test_add_card_version(self):
        pass

    def test_remove_card_version(self):
        pass

    def test_add_possession(self):
        pass

    def test_remove_possession(self):
        pass

    def test_add_game(self):
        pass

    def test_remove_game(self):
        pass
