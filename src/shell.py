#!/usr/bin/env python3

import cmd
import cards_bd
import update_card_db
import pymysql
import os
import shell_add as sa
import shell_remove as sr


tables = [
    {"name": "card", "add": sa.add_card, "remove": sr.remove_card},
    {"name": "player", "add": sa.add_player, "remove": sr.remove_player},
    {"name": "version", "add": sa.add_version, "remove": sr.remove_version},
    {"name": "possession", "add": sa.add_possession, "remove": sr.remove_possession},
    {"name": "deck", "add": sa.add_deck, "remove": sr.remove_deck},
    {"name": "membership", "add": sa.add_, "remove": sr.remove_},
    {"name": "game", "add": sa.add_game, "remove": sr.remove_game},
    {"name": "play", "add": sa.add_play, "remove": sr.remove_play},
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
                print(" - {}".format(table["name"]))
            print()

    def do_remove(self, arg):
        "Remove an element"
        if arg:
            table = arg.split(" ")[0]
            if table in [t["name"] for t in tables]:
                t_dict = [t for t in tables if t["name"] == table][0]
                t_dict["remove"](self.conn)
            else:
                print("Error: table '{}' is not valid".format(table))
        else:
            print("\nChoose one of this:")
            for table in tables:
                print(" - {}".format(table["name"]))
            print()

    def do_list(self, arg):
        "List an element"
        if arg:
            table = arg.split(" ")[0]
            if table[:-1] in [t["name"] for t in tables]:
                cur = cards_bd.db_execute(self.conn, cards_bd.sql_src["list"][table])
                result = cur.fetchall()
                if result:
                    for key in result[0]:
                        print("{:^10s}".format(key), end="|")
                    print()
                    for res in result:
                        for item in res.values():
                            print(
                                "{:^10s}".format(str(item) if item else "None"),
                                end="|",
                            )
                        print()
            else:
                print("Error: table '{}' is not valid".format(table))
        else:
            print("\nSyntax:\n\t`list <table>`\nwhere <table> is one of this:")
            for table in tables:
                print(" - {}s".format(table["name"]))
            print()

    def do_consult(self, arg):
        "Consultations"
        print("Consult")

    def do_statistics(self, arg):
        "Statistics"
        print("Statistics")

    def emptyline(self):
        pass

    def do_quit(self, arg):
        print("Close")


if __name__ == "__main__":
    SqlShell().cmdloop()
