##
# SGBD
#
# @file
# @version 0.1

# --- Directories ---
SRC_DIR = src
TST_DIR = test

# --- Build rules ---
run:
	python3 $(SRC_DIR)/main.py

test:
	python3 $(TST_DIR)/main.py

# end
