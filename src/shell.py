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

consultations = [
    {"name": "cards_by_type", "function": cards_bd.cards_by_type},
    {"name": "cards_in_possession", "function": cards_bd.cards_in_possession},
    {"name": "cards_not_in_deck", "function": cards_bd.cards_not_in_deck},
    {"name": "players_collectors", "function": cards_bd.players_collectors},
]

statistics = [
    {"name": "player_nb_cards", "function": cards_bd.player_nb_cards},
    {"name": "players_by_value", "function": cards_bd.players_by_value},
    {"name": "cards_in_decks", "function": cards_bd.cards_in_decks},
    {"name": "player_rare_collectors", "function": cards_bd.player_rare_collectors},
    {"name": "cards_familly", "function": cards_bd.cards_familly},
]

host = os.environ["DB_HOST"]
user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]


def sql_display(data):
    print("\n+", end="")
    for key in data[0]:
        print("{:-^20}".format(""), end="+")
    print("\n|", end="")
    for key in data[0]:
        print("{:^20.20}".format(key), end="|")
    print("\n+", end="")
    for key in data[0]:
        print("{:-^20}".format(""), end="+")
    for res in data:
        print("\n|", end="")
        for item in res.values():
            print(
                "{:^20.20}".format(str(item) if item else "None"), end="|",
            )
    print("\n+", end="")
    for key in data[0]:
        print("{:-^20}".format(""), end="+")
    print("\n")


def list_table(conn, table):
    cur = cards_bd.db_execute(conn, cards_bd.sql_src["list"][table])
    results = cur.fetchall()
    if results:
        sql_display(results)


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
                t_dict["remove"](self.conn, arg.split(" ")[1:])
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
                list_table(self.conn, table)
            else:
                print("Error: table '{}' is not valid".format(table))
        else:
            print("\nSyntax:\n\t`list <table>`\nwhere <table> is one of this:")
            for table in tables:
                print(" - {}s".format(table["name"]))
            print()

    def do_consult(self, arg):
        "Consultations"
        if arg:
            consultation = arg.split(" ")[0]
            if consultation in [c["name"] for c in consultations]:
                c_dict = [t for t in consultations if t["name"] == consultation][0]
                if len(arg.split(" ")) > 1:
                    data = c_dict["function"](self.conn, arg.split(" ")[1]).fetchall()
                else:
                    data = c_dict["function"](self.conn).fetchall()

                if data:
                    sql_display(data)

            else:
                print("Error: consultation '{}' is not valid".format(consultation))
        else:
            print("\nChconsult one of this:")
            for c in consultations:
                print(" - {}".format(c["name"]))
            print()

    def do_statistics(self, arg):
        "Statistics"
        if arg:
            statistic = arg.split(" ")[0]
            if statistic in [c["name"] for c in statistics]:
                c_dict = [t for t in statistics if t["name"] == statistic][0]
                if len(arg.split(" ")) > 1:
                    data = c_dict["function"](self.conn, arg.split(" ")[1]).fetchall()
                else:
                    data = c_dict["function"](self.conn).fetchall()

                if data:
                    sql_display(data)

            else:
                print("Error: statistic '{}' is not valid".format(statistic))
        else:
            print("\nChconsult one of this:")
            for c in statistics:
                print(" - {}".format(c["name"]))
            print()

    def do_populate(self, arg):
        "Populate tables"
        if arg:
            args = arg.split(" ")
            for path in args:
                update_card_db.populate_tables(self.conn, path)
                print("Successfully loaded file {}".format(path))
        else:
            print("\nPlease specify a sql file to load")

    def complete_add(self, text, line, begidx, endidx):
        if len(line.split(" ")) > 2:
            list_table(self.conn, line.split(" ")[1] + "s")
            return [""]
        return [t["name"] for t in tables if t["name"].startswith(text)]

    def complete_remove(self, *args):
        return self.complete_add(*args)

    def complete_list(self, text, line, begidx, endidx):
        return [t["name"] + "s" for t in tables if t["name"].startswith(text)]

    def complete_consult(self, text, line, begidx, endidx):
        return [c["name"] for c in consultations if c["name"].startswith(text)]

    def complete_statistics(self, text, line, begidx, endidx):
        return [s["name"] for s in statistics if s["name"].startswith(text)]

    def emptyline(self):
        pass

    def do_quit(self, arg):
        self.conn.close()
        exit()


if __name__ == "__main__":
    SqlShell().cmdloop()
