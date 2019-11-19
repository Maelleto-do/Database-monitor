#!/usr/bin/env python3.7

import sys
import os
import unittest

# (dev only) add the parent package to PYTHONPATH 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import cards_bd

class TestStats(unittest.TestCase):
    """Unit tests for the stats request"""

    def test_player_list(self):
        pass

    def test_players_by_value(self):
        pass

    def test_cards_in_decks(self):
        pass

    def test_player_rare_collectors(self):
        pass

    def test_cards_family(self):
        pass
