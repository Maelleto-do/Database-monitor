#!/usr/bin/env python3.7

import cmd
import cards_bd
import update_card_db
import pymysql
import os

tables = [
    "cards",
    "players",
    "versions",
    "possessions",
    "decks",
    "memberships",
    "games",
    "plays",
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
            print("not implemented")
        else:
            print("\nChoose one of this:")
            for table in tables:
                print(" - {}".format(table))
            print()

    def do_remove(self, arg):
        "Remove an element"
        if arg:
            print("not implemented")
        else:
            print("\nChoose one of this:")
            for table in tables:
                print(" - {}".format(table))
            print()

    def do_list(self, arg):
        "List an element"
        if arg:
            table = arg.split(" ")[0]
            if table in tables:
                cur = cards_bd.db_execute(self.conn, cards_bd.sql_src["list"][table])
            else:
                print("Error: table '{}' is not valid".format(table))
        else:
            print("\nSyntax:\n\t`list <table>`\nwhere <table> is one of this:")
            for table in tables:
                print(" - {}".format(table))
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
