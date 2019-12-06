#!/usr/bin/env python3

import yaml
import os

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


def cards_by_type(conn):
    """List cards of a certain type."""
    pass


def cards_not_in_deck(conn):
    """List cards not in a deck."""
    pass


def players_collectors(conn):
    """List players that didn't participated in a game."""
    pass


# Statistic


def player_list(conn):
    """List players and the number of cards they own."""
    sql_req = cards_bd.sql_src["player_list"]
    cards_bd.db_execute(conn, sql_req)
    


def players_by_value(conn):
    """List player in descending order by the value of their collection."""
    pass


def cards_in_decks(conn):
    """List cards and the number of players that use them in their decks."""
    pass


def player_rare_collectors(conn):
    """List players who own the maximum of rare card."""
    pass


def cards_family(conn):
    """List card family and the caracteristic in which this family has the best level."""
    pass
