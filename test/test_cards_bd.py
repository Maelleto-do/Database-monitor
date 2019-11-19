#!/usr/bin/env python3.7

import sys
import os
import unittest

# (dev only) add the parent package to PYTHONPATH 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import cards_bd

class SGBDCarteTest(unittest.TestCase):
    """Unit tests for the cartes_db library"""

    def test_create_db(self):
        pass

    def test_drop_dp(self):
        pass

    def test_cards_by_type(self):
        pass

    def test_cards_not_in_deck(self):
        pass

    def test_players_collectors(self):
        pass

    def test_player_list(self):
        pass

    def test_players_by_value(self):
        pass

    def test_cards_in_deck(self):
        pass

    def test_player_rate_collectors(self):
        pass

    def test_cards_family(self):
        pass

if __name__ == "__main__":
    unittest.main()