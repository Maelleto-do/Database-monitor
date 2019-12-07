##
# SGBD
#
# @file
# @version 0.1

# --- Directories ---
SRC_DIR = src
TST_DIR = test

# --- Environnement variables ---
include .env
export

# --- Build rules ---
.PHONY: test

run:
	python3 $(SRC_DIR)/main.py

test: $(TST_DIR)/*
	python3 $(TST_DIR)/test_cards_bd.py

shell:
	python3 $(SRC_DIR)/shell.py

# end
