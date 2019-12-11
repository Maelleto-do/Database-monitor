#!/usr/bin/env python3.7

import update_card_db


def add_(conn):
    print("not implemented")


def remove_(conn):
    print("not implemented")


def shell_input(message=None, required=False):
    return input(message)


def add_card(conn):
    title = shell_input("Card title (Required): ", True)
    description = shell_input("Card description: ")
    familly = shell_input("Card familly: ")
    attack = shell_input("Card attack: ")
    defense = shell_input("Card defense: ")
    attack = attack if attack else None
    defense = defense if defense else None
    update_card_db.add_card(conn, title, description, familly, attack, defense)


def add_player(conn):
    pseudo = shell_input("Player pseudo (Required): ", True)
    name = shell_input("Player name: ")
    first_name = shell_input("Player first name: ")
    update_card_db.add_player(conn, pseudo, name, first_name)


def add_deck(conn):
    deck_name = shell_input("Deck name (Required): ", True)
    pseudo = shell_input("Deck owner (Required): ", True)
    update_card_db.add_deck(conn, deck_name, pseudo)


def add_version(conn):
    id_card = shell_input("Card id (Required): ", True)
    rendering = shell_input("Version rendering: ")
    rating = shell_input("Version rating: ")
    print_run = shell_input("Version print_run: ")
    rating = rating if rating else None
    print_run = print_run if print_run else None
    update_card_db.add_card_version(conn, id_card, rendering, rating, print_run)


def add_possession(conn):
    pseudo = shell_input("Owner (Required): ", True)
    id_version = shell_input("Version id: ")
    purchase_date = shell_input("Purchase date (YYYY/MM/DD): ")
    purchase_date = purchase_date if purchase_date else None
    purchase_mode = shell_input("Purchase mode: ")
    sale_date = shell_input("Sale date (YYYY/MM/DD): ")
    sale_date = sale_date if sale_date else None
    sale_price = shell_input("Sale price: ")
    sale_price = sale_price if sale_price else None
    state = shell_input("State: ")
    state = state if state else None
    update_card_db.add_possession(
        conn,
        pseudo,
        id_version,
        purchase_date,
        purchase_mode,
        sale_date,
        sale_price,
        state,
    )


def add_play(conn):
    id_game = shell_input("Game id (Required): ", True)
    id_deck = shell_input("Deck id (Required): ", True)
    pseudo = shell_input("Player (Required): ", True)
    update_card_db.add_play(conn, id_game, id_deck, pseudo)


def add_game(conn):
    game_date = shell_input("Game date (Required)(YYYY/MM/DD): ", True)
    game_location = shell_input("Game location: ")
    tournament_type = shell_input("Type of tournament: ")
    update_card_db.add_game(
        conn, game_date, game_location, tournament_type, game_results
    )


def add_membership(conn):
    id_possession = shell_input("Possession id (Required): ", True)
    id_deck = shell_input("Deck id (Required): ", True)
    update_card_db.add_membership(conn, id_possession, id_deck)