#!/usr/bin/env python3

import yaml
import os
import logging

logging.basicConfig(level=logging.DEBUG)

script_dir = os.path.dirname(__file__)
yaml_file = script_dir + "/sql_src.yaml"

global sql_src


def db_execute(conn, sql, args=None):
    """Wrapper to execute a command to the database."""
    affected_rows = 0
    with conn.cursor() as cur:
        affected_rows = cur.execute(sql, args)
    conn.commit()
    return cur


def load_commands(commands_file):
    global sql_src
    with open(commands_file, "r") as stream:
        try:
            sql_src = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def init():
    load_commands(yaml_file)


def close():
    pass


# Consultation


def cards_by_type(conn, card_type):
    """List cards of a certain type."""
    sql_req = sql_src["consultation"]["cards_by_type"]
    db_execute(conn, sql_req, card_type)
    logging.debug("Consulted cards of type '%s'", card_type)


def cards_in_possession(conn):
    """List cards that are or have been owned by a player."""
    sql_req = sql_src["consultation"]["cards_in_possession"]
    db_execute(conn, sql_req)
    logging.debug("Consulted cards owned by players")


def cards_not_in_deck(conn):
    """List cards that are not in any deck"""
    sql_req = sql_src["consultation"]["cards_not_in_deck"]
    db_execute(conn, sql_req)
    logging.debug("Consulted cards that are not in any deck")



def players_collectors(conn):
    """List players that didn't participated in a game."""
    sql_req = sql_src["consultation"]["players_collector"]
    db_execute(conn, sql_req)
    logging.debug("Consulted players that have not played (collectors)")


# Statistic


def player_nb_cards(conn):
    """List players and the number of cards they own."""
    sql_req = sql_src["stats"]["player_nb_cards"]
    db_execute(conn, sql_req)
    logging.debug("Consulted stats for the number of cards per player")


def players_by_value(conn):
    """List player in descending order by the value of their collection."""
    sql_req = sql_src["stats"]["players_by_value"]
    db_execute(conn, sql_req)
    logging.debug("Consulted stats for listing players in descending order by the value of their collection")


def cards_in_decks(conn):
    """List cards and the number of players that use them in their decks."""
    sql_req = sql_src["stats"]["cards_in_decks"]
    db_execute(conn, sql_req)
    logging.debug("Consulted stats for cards and the number of players that use them in their decks")



def player_rare_collectors(conn):
    """List players who own the maximum of rare card."""
    sql_req = sql_src["stats"]["cards_in_decks"]
    db_execute(conn, sql_req)
    logging.debug("Consulted stats for players who own the maximum of rare card")


def cards_family(conn):
    """List card family and the caracteristic in which this family has the best level."""
    pass
