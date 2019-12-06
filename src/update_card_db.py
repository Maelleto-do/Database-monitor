#!/usr/bin/env python3

import cards_bd
import logging


def create_tables(conn):
    """Create the card database"""
    for table, sql_req in cards_bd.sql_src["create_table"].items():
        cards_bd.db_execute(conn, sql_req)
        logging.debug("'%s' table created", table)


def drop_tables(conn):
    """Delete the card database"""
    for table, sql_req in cards_bd.sql_src["drop_table"].items():
        cards_bd.db_execute(conn, sql_req)
        logging.debug("'%s' table dropped", table)


def add_player(conn, pseudo, nom, prenom):
    """Add a player in the database"""
    cards_bd.db_execute(conn, cards_bd.sql_src["insert_player"], [pseudo, nom, prenom])


def remove_player(conn, pseudo):
    """Remove a player from the database"""
    cards_bd.db_execute(conn, cards_bd.sql_src["remove_player"], pseudo)


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
