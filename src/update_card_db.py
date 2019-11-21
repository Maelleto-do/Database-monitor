#!/usr/bin/env python3

import cards_bd
import logging

def create_db(conn):
    """Create the card database"""
    cards_bd.db_execute(conn, cards_bd.sql_src["create_cards_table"])
    logging.debug("'cartes' table created")
    cards_bd.db_execute(conn, cards_bd.sql_src["create_cards_table"])
    logging.debug("'versions' table created")

def drop_db(conn):
    """Delete the card database"""
    pass


def add_player(conn):
    pass


def remove_player(conn):
    pass


def add_deck(conn):
    pass


def remove_deck(conn):
    pass


def add_card(conn):
    pass


def remove_card(conn):
    pass


def add_card_version(conn):
    pass


def remove_card_version(conn):
    pass


def add_possession(conn):
    pass


def remove_possession(conn):
    pass


def add_game(conn):
    pass


def remove_game(conn):
    pass
