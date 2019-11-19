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
        pass

    def test_cards_not_in_deck(self):
        pass

    def test_players_collectors(self):
        pass
