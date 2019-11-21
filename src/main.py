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

    update_card_db.create_tables(conn)
    update_card_db.drop_tables(conn)


if __name__ == "__main__":
    main()
