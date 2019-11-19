#!/usr/bin/env python3.7

import sys
import os
import unittest

# (dev only) add the parent package to PYTHONPATH 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import cards_bd

class TestUpdate(unittest.TestCase):
    """Unit tests for the update request"""

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
