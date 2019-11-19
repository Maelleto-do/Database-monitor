#!/usr/bin/env python3.7

import sys
import os
import unittest

# (dev only) add the parent package to PYTHONPATH 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import cards_bd

class TestConsultation(unittest.TestCase):
    """Unit tests for the consultation request"""

    def test_cards_by_type(self):
        pass

    def test_cards_not_in_deck(self):
        pass

    def test_players_collectors(self):
        pass