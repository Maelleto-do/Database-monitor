-- CONSULTATION

-- Show cards of a certain familly
    SELECT * FROM `cards` WHERE `familly` = %s;

-- Show cards that are possessed by a player
    SELECT DISTINCT `title`, `familly`, `attack`, `defense`, `rendering`, `print_run`, `rating` FROM (`cards` NATURAL JOIN `versions`) NATURAL JOIN `possessions` ;

-- Show cards that are not in any deck
    SELECT DISTINCT `title`, `familly`, `attack`, `defense`, `rendering`, `print_run`, `rating` FROM (`cards` NATURAL JOIN `versions`) WHERE versions.id_version NOT IN
    (SELECT DISTINCT versions.id_version FROM (`cards` NATURAL JOIN `versions`) NATURAL JOIN `possessions`);

--  Show players that do not have any deck
    SELECT DISTINCT `pseudo` FROM `players` WHERE players.pseudo NOT IN (SELECT `pseudo` FROM `plays`);


-- STATS

--  Players and their number of cards
SELECT DISTINCT pseudo, count(*) AS 'NB CARDS' FROM possessions GROUP BY pseudo;

-- Players and the value of their collection
SELECT P.pseudo, SUM((rating * P.state)) as 'TOTAL RATE' 
FROM possessions P, versions V
where P.id_version = V.id_version
group by P.pseudo;

--  All cards that are in a deck
SELECT D.title, count(*) as 'NB_PLAYERS' 
FROM (
     SELECT DISTINCT C.id_card, C.title, S.pseudo FROM
     versions V, (SELECT DISTINCT id_possession, id_version, D.pseudo FROM 
     possessions P, decks D 
     where P.pseudo = D.pseudo) as S, cards C
      where S.id_version = V.id_version
      and C.id_card = V.id_card
    ) as D
    group by D.id_card; 
  
-- Player that have rare cards
SELECT MAX(A.total) as 'maxRate' FROM 
    (
      SELECT P.pseudo, SUM((rating * P.state)) as 'total' FROM
      possessions P, versions V
      where P.id_version = V.id_version
      group by P.pseudo
    ) as A;
  
-- Best stat of each family
SELECT familly, 
      CASE
          WHEN A.attack = 0 AND A.defense = 0 THEN 'attack and defense level at zero'
          WHEN A.attack = A.defense THEN 'best for attack and defense'
          WHEN A.attack >= A.defense THEN 'best for attack'
          else 'best for defense'
      END AS BestLevelCaracteristic
    FROM 
    (
      SELECT familly, SUM(attack) as 'attack', SUM(defense) as 'defense' FROM
      cards
      group by familly
    ) as A; 
