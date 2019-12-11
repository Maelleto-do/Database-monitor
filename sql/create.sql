-- CREATE ALL BASES 

-- CARDS
CREATE TABLE IF NOT EXISTS cards (
        id_card INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        title TEXT,
        description TEXT,
        familly VARCHAR(64),
        attack INT,
        defense INT
);

-- VERSIONS
CREATE TABLE IF NOT EXISTS versions (
      id_version INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
      id_card INT UNSIGNED,
      rendering VARCHAR(64),
      rating INT,
      print_run INT,
      FOREIGN KEY (id_card) REFERENCES cards(id_card)
);

-- PLAYERS
CREATE TABLE IF NOT EXISTS players (
      pseudo VARCHAR(64) PRIMARY KEY,
      player_name VARCHAR(64),
      player_first_name VARCHAR(64)
);

-- POSSESSIONS
CREATE TABLE IF NOT EXISTS possessions (
      id_possession INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
      pseudo VARCHAR(64),
      id_version INT UNSIGNED,
      purchase_date DATE,
      purchase_mode VARCHAR(64),
      sale_date DATE,
      sale_price INT,
      state INT,
      FOREIGN KEY (pseudo) REFERENCES players(pseudo),
      FOREIGN KEY (id_version) REFERENCES versions(id_version)
);

-- DECKS
CREATE TABLE IF NOT EXISTS decks (
      id_deck INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
      deck_name VARCHAR(64),
      pseudo VARCHAR(64),
      FOREIGN KEY (pseudo) REFERENCES players(pseudo)
);

-- MEMBERSHIPS
CREATE TABLE IF NOT EXISTS memberships (
      id_possession INT UNSIGNED,
      id_deck INT UNSIGNED,
      CONSTRAINT membership_pk PRIMARY KEY (id_possession, id_deck),
      FOREIGN KEY (id_possession) REFERENCES possessions(id_possession),
      FOREIGN KEY (id_deck) REFERENCES decks(id_deck)
);

-- GAMES
CREATE TABLE IF NOT EXISTS games (
      id_game INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
      game_date DATE,
      game_location VARCHAR(64),
      tournament_type VARCHAR(64),
      game_results VARCHAR(64),
      FOREIGN KEY (game_results) REFERENCES players(pseudo)
);

-- PLAYS
CREATE TABLE IF NOT EXISTS plays (
      id_game INT UNSIGNED,
      id_deck INT UNSIGNED,
      pseudo VARCHAR(64),
      FOREIGN KEY (id_game) REFERENCES games(id_game),
      FOREIGN KEY (id_deck) REFERENCES decks(id_deck),
      FOREIGN KEY (pseudo) REFERENCES players(pseudo),
      PRIMARY KEY (id_game, id_deck, pseudo)
);
