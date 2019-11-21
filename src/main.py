#!/usr/bin/env python3.7

import cards_bd
import update_card_db
import logging

logging.basicConfig(level=logging.DEBUG)

def main():
    cards_bd.init()
    update_card_db.create_db(None)
    # print(cards_bd.sql_src)

if __name__ == "__main__":
    main()
