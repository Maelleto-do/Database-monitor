#!/usr/bin/env python3.7

import sys
import os
import unittest
import pymysql

# (dev only) add the parent package to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src import cards_bd

host = os.environ["DB_HOST"]
user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


class TestConsultation(unittest.TestCase):
    """Unit tests for the consultation request"""

    def __init__(self, *args, **kwargs):
        super(TestConsultation, self).__init__(*args, **kwargs)
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db_name,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def test_cards_by_type(self):
        cur = cards_bd.cards_by_type(self.conn, "Dark")
        res = cur.fetchall()
        self.assertEqual(cur.rowcount(), 3, "error in test_cards_by_type")
        
    def test_cards_in_possession(self):
        cur = cards_bd.cards_by_type(self.conn, "Dark")
        res = cur.fetchall()
        self.assertEqual(cur.rowcount(), 12, "error in test_cards_in_possession")

    def test_cards_not_in_deck(self):
        cur = cards_bd.cards_in_possession(self.conn)
        res = cur.fetchall()
        self.assertEqual(cur.rowcount(), 7, "error in test_cards_not_in_deck")
        

    def test_players_collectors(self):
        cur = cards_bd.players_collectors(self.conn)
        res = cur.fetchall()
        self.assertEqual(cur.rowcount(), 0, "error in test_players_collectors")
        
