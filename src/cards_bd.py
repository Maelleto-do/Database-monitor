#!/usr/bin/env python3

import yaml

def db_execute(conn, sql, args):
    """Wrapper to execute a command to the database."""
    with conn.cursor() as cur:
        cur.execute(sql, args)
    conn.commit()

def load_commands(commands_file):
    global sql_src
    with open(commands_file, 'r') as stream:
        try:
            sql_src = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def init():
    load_commands("sql_src.yaml")

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
    pass


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
