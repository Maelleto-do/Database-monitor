#!/usr/bin/env python3.7

import cmd
import cards_bd
import update_card_db
import pymysql
import os


def add_(conn):
    print("not implemented")


def remove_(conn):
    print("not implemented")


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


def shell_input(message=None, required=False):
    return input(message)


tables = [
    {"name": "card", "add": add_card, "remove": remove_},
    {"name": "player", "add": add_player, "remove": remove_},
    {"name": "version", "add": add_, "remove": remove_},
    {"name": "possession", "add": add_, "remove": remove_},
    {"name": "deck", "add": add_deck, "remove": remove_},
    {"name": "membership", "add": add_, "remove": remove_},
    {"name": "game", "add": add_, "remove": remove_},
    {"name": "play", "add": add_, "remove": remove_},
]

host = os.environ["DB_HOST"]
user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


class SqlShell(cmd.Cmd):
    """Documentation"""

    intro = "Welcome to our card shell.   Type help or ? to list commands.\n"
    prompt = "> "

    def __init__(self):
        cmd.Cmd.__init__(self)
        cards_bd.init()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db_name,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        update_card_db.create_tables(self.conn)

    def do_add(self, arg):
        "Add an element:\n\tadd <element> <args>"
        if arg:
            table = arg.split(" ")[0]
            if table in [t["name"] for t in tables]:
                t_dict = [t for t in tables if t["name"] == table][0]
                t_dict["add"](self.conn)
            else:
                print("Error: table '{}' is not valid".format(table))
        else:
            print("\nChoose one of this:")
            for table in tables:
                print(" - {}".format(table["name"][:-1]))
            print()

    def do_remove(self, arg):
        "Remove an element"
        if arg:
            print("not implemented")
        else:
            print("\nChoose one of this:")
            for table in tables:
                print(" - {}".format(table["name"][:-1]))
            print()

    def do_list(self, arg):
        "List an element"
        if arg:
            table = arg.split(" ")[0]
            if table[:-1] in [t["name"] for t in tables]:
                cur = cards_bd.db_execute(self.conn, cards_bd.sql_src["list"][table])
                for res in cur.fetchall():
                    print(res)
            else:
                print("Error: table '{}' is not valid".format(table))
        else:
            print("\nSyntax:\n\t`list <table>`\nwhere <table> is one of this:")
            for table in tables:
                print(" - {}s".format(table["name"][:-1]))
            print()

    def do_consult(self, arg):
        "Consultations"
        print("Consult")

    def do_statistics(self, arg):
        "Statistics"
        print("Statistics")

    def do_quit(self, arg):
        print("Close")


if __name__ == "__main__":
    SqlShell().cmdloop()
