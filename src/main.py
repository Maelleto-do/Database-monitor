#!/usr/bin/env python3.7

import cards_bd
import update_card_db
import logging
import os
import pymysql

logging.basicConfig(level=logging.DEBUG)


def connect_db():

    host = os.environ["DB_HOST"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    db_name = os.environ["DB_NAME"]

    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db_name,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def main():
    conn = connect_db()
    cards_bd.init()

<<<<<<< HEAD
=======
    update_card_db.create_tables(conn)
    update_card_db.add_player(conn, 'totoPeusdo', 'toto', 'tata')
    # update_card_db.drop_tables(conn)
    # print(cards_bd.sql_src)
    # update_card_db.drop_tables(conn)
>>>>>>> ad3c5c6fe11fcd411b2b11b18238084c2cc49dd7

    update_card_db.create_tables(conn)
    # update_card_db.add_deck(conn, 'myDeckTest', 'pseudoTest')
    # update_card_db.add_card(conn, "roudoudou", "rose", "pokemon", attaque=0, defense=0)
    # update_card_db.add_card(conn, "pikachu", "jaune", "pokemon", attaque=0, defense=0)
    # update_card_db.add_card_version(conn, 1, rendu="Normal", cote=0, tirage=0)
    # update_card_db.add_possession(conn, 'myDeckTest', 'pseudoTest')

if __name__ == "__main__":
    main()
