#!/usr/bin/env python3

import cards_bd
import logging

logging.basicConfig(level=logging.ERROR)


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


def add_player(conn, pseudo, nom=None, prenom=None):
    """Add a player in the database"""
    sql_req = cards_bd.sql_src["add"]["deck"]
    cards_bd.db_execute(conn, sql_req, (pseudo, nom, prenom))


def remove_player(conn, pseudo):
    """Remove a player from the database"""
    sql_req = cards_bd.sql_src["remove"]["player"]
    cards_bd.db_execute(conn, sql_req, pseudo)


def add_deck(conn, nom_deck, pseudo):
    """Add a deck"""
    sql_req = cards_bd.sql_src["add"]["deck"]
    cards_bd.db_execute(conn, sql_req, (nom_deck, pseudo))
    logging.debug("Added deck '%s' for pseudo '%s'", nom_deck, pseudo)


def remove_deck(conn, nom_deck):
    sql_req = cards_bd.sql_src["remove"]["deck"]
    cards_bd.db_execute(conn, sql_req, nom_deck)
    logging.debug("Removed deck '%s'", nom_deck)


def add_card(conn, title, description="", famille="", attaque=0, defense=0):
    sql_req = cards_bd.sql_src["add"]["card"]
    cards_bd.db_execute(conn, sql_req, (title, description, famille, attaque, defense))
    logging.debug("Added card '%s'", title)


def remove_card(conn, id_card):
    sql_req = cards_bd.sql_src["remove"]["card"]
    logging.debug("Removed card '%s'", id_card)
    cards_bd.db_execute(conn, sql_req, id_card)


def add_card_version(conn, id_carte, rendu="Normal", cote=0, tirage=0):
    sql_req = cards_bd.sql_src["add"]["version"]
    cards_bd.db_execute(conn, sql_req, (id_carte, rendu, cote, tirage))
    logging.debug("Added version '%s' for card %s", rendu, id_carte)


def remove_card_version(conn, id_version):
    sql_req = cards_bd.sql_src["remove"]["version"]
    cards_bd.db_execute(conn, sql_req, id_version)
    logging.debug("Removed version '%s'", id_version)


def add_possession(
    conn,
    pseudo,
    id_version,
    purchase_date=None,
    purchase_mode=None,
    sale_date=None,
    sale_price=None,
    state=None,
):
    sql_req = cards_bd.sql_src["add"]["possession"]
    cards_bd.db_execute(
        conn,
        sql_req,
        (
            pseudo,
            id_version,
            purchase_date,
            purchase_mode,
            sale_date,
            sale_price,
            state,
        ),
    )
    logging.debug("Added possession for pseudo '%s'", pseudo)


def remove_possession(conn, id_possession):
    sql_req = cards_bd.sql_src["remove"]["possession"]
    cards_bd.db_execute(conn, sql_req, id_possession)
    logging.debug("Removed possession '%s'", id_possession)


def add_game(conn, date_partie, lieu_partie, type_tournoi, resultat_partie):
    sql_req = cards_bd.sql_src["add"]["game"]
    cards_bd.db_execute(
        conn, sql_req, (date_partie, lieu_partie, type_tournoi, resultat_partie)
    )
    logging.debug("Added game")


def remove_game(conn, id_game):
    sql_req = cards_bd.sql_src["remove"]["game"]
    cards_bd.db_execute(conn, sql_req, (id_game))
    logging.debug("Removed game '%s'", id_game)
