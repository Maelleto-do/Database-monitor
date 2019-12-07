#!/usr/bin/env python3

import update_card_db


def remove_(conn):
    print("not implemented")


def shell_input(message=None, required=False):
    return input(message)


def remove_card(conn):
    identifiant = shell_input("Card id (Required): ", True)
    update_card_db.remove_card(conn, identifiant)


def remove_player(conn):
    identifiant = shell_input("Pseudo (Required): ", True)
    update_card_db.remove_player(conn, identifiant)


def remove_deck(conn):
    identifiant = shell_input("Deck id (Required): ", True)
    update_card_db.remove_deck(conn, identifiant)


def remove_version(conn):
    identifiant = shell_input("Version id (Required): ", True)
    update_card_db.remove_version(conn, identifiant)


def remove_possession(conn):
    identifiant = shell_input("Possession id (Required): ", True)
    update_card_db.remove_possession(conn, identifiant)


def remove_play(conn):
    identifiant = shell_input("Play id (Required): ", True)
    update_card_db.remove_play(conn, identifiant)


def remove_game(conn):
    identifiant = shell_input("Game id (Required): ", True)
    update_card_db.remove_game(conn, identifiant)
