-- ============================================================
--    delete data (not tables)
-- ============================================================

delete from PLAYS ;
delete from GAMES ;
delete from MEMBERSHIPS ;
delete from DECKS ;
delete from POSSESSIONS ;
delete from PLAYERS ;
delete from VERSIONS ;
delete from CARDS ;

commit ;

-- ============================================================
--    populate tables
-- ============================================================

-- CARDS

alter table CARDS AUTO_INCREMENT = 1;
insert into CARDS values (NULL, 'Lancephorhynchus', 'Weird dragon', 'Wind', 2500, 800) ;
insert into CARDS values (NULL, 'Edge Imp Sabres',  'It''s an imp', 'Dark', 1200, 800) ;
insert into CARDS values (NULL, 'Qliphort Carrier', 'Strange name', 'Earth', 2400, 1000) ;
insert into CARDS values (NULL, 'Qliphort Helix', 'Carrier''s brother', 'Earth', 2400, 1000)  ;
insert into CARDS values (NULL, 'Taotie, Shadow of the Yang Zing', 'Dog', 'Dark', 2200, 0) ;
insert into CARDS values (NULL, 'Machina Megaform', 'Big robot', 'Eath', 2600, 1500) ;
insert into CARDS values (NULL, 'Rescue Hamster', 'Cute', 'Earth', 300, 100) ;
insert into CARDS values (NULL, 'First of the Dragons', 'Dragon fusion', 'Dark', 2700, 2000) ;
insert into CARDS values (NULL, 'Herald of the Arc Light', 'Fairy synchro', 'Light', 600, 1000) ;
insert into CARDS values (NULL, '1st movement solo', 'Summon something', 'Spell', 0, 0) ;
insert into CARDS values (NULL, 'El Shaddoll Fusion', 'It''s a fusion', 'Spell', 0, 0) ;
insert into CARDS values (NULL, 'First Lake of the Burning Abyss', 'It''s a trap!', 'Trap', 0, 0) ;
insert into CARDS values (NULL, 'Number 39: Utopia Beyond', 'Warrior', 'Light', 3000, 2500) ;
insert into CARDS values (NULL, 'CXyz Barian Hope', 'Warrior', 'Light', 0, 0) ;

commit ;

-- versions

alter table versions AUTO_INCREMENT = 1;
insert into versions values (NULL, 1, 'NORMAL', 5, 2000) ;
insert into versions values (NULL, 2, 'NORMAL', 5, 5000) ;
insert into versions values (NULL, 3, 'NORMAL', 5, 10000) ;
insert into versions values (NULL, 4, 'NORMAL', 5, 2000) ;
insert into versions values (NULL, 5, 'NORMAL', 5, 7000) ;
insert into versions values (NULL, 6, 'NORMAL', 5, 8000) ;
insert into versions values (NULL, 7, 'NORMAL', 5, 2000) ;
insert into versions values (NULL, 8, 'NORMAL', 5, 9000) ;
insert into versions values (NULL, 9, 'NORMAL', 5, 2000) ;
insert into versions values (NULL, 10, 'NORMAL', 5, 2000) ;
insert into versions values (NULL, 11, 'NORMAL', 5, 6000) ;
insert into versions values (NULL, 12, 'NORMAL', 5, 7000) ;
insert into versions values (NULL, 13, 'NORMAL', 5, 3000) ;
insert into versions values (NULL, 14, 'NORMAL', 5, 4000) ;
insert into versions values (NULL, 1, 'SHINY', 20, 1000) ;
insert into versions values (NULL, 2, 'SHINY', 30, 1000) ;
insert into versions values (NULL, 3, 'SHINY', 50, 1000) ;
insert into versions values (NULL, 4, 'SHINY', 39, 1000) ;
insert into versions values (NULL, 5, 'SHINY', 100, 1000) ;

commit ;

-- PLAYERS

insert into PLAYERS values ('Matodo', 'Maelle', 'Toy-Riont--Le-Dosseur') ;
insert into PLAYERS values ('Boytus', 'Lucas', 'Henry') ; 
insert into PLAYERS values ('Toastation', 'Melvin', 'Even') ;
insert into PLAYERS values ('Gouvernathor', 'Pierre', 'Tavia') ; 

commit ;

-- possessions 

alter table possessions AUTO_INCREMENT = 1;

insert into possessions values (NULL, 'Matodo', 1, '2019-09-28', 'NEUF', NULL, NULL, 90) ;
insert into possessions values (NULL, 'Matodo', 6, '2019-02-12', 'NEUF', '2019-06-08', 9, 96) ;
insert into possessions values (NULL, 'Matodo', 4, '2019-09-28', 'NEUF', NULL, NULL, 90) ;
insert into possessions values (NULL, 'Matodo', 17, '2019-09-28', 'OCCASION', NULL, NULL, 40) ;
insert into possessions values (NULL, 'Matodo', 10, '2019-09-28', 'OCCASION', NULL, NULL, 70) ;
insert into possessions values (NULL, 'Matodo', 11, '2019-09-28', 'NEUF', NULL, NULL, 70) ;
insert into possessions values (NULL, 'Matodo', 14, '2019-01-01', 'OCCASION', '2019-04-6', -1, 20) ;

insert into possessions values (NULL, 'Boytus', 1, '2019-04-18', 'NEUF', NULL, NULL, 70) ;
insert into possessions values (NULL, 'Boytus', 6, '2019-01-13', 'OCCASION', '2019-04-19', 4, 56) ;
insert into possessions values (NULL, 'Boytus', 4, '2019-05-25', 'NEUF', NULL, NULL, 80) ;
insert into possessions values (NULL, 'Boytus', 17, '2019-03-03', 'OCCASION', NULL, NULL, 10) ;

insert into possessions values (NULL, 'Toastation', 1, '2019-04-12', 'NEUF', NULL, NULL, 90) ;
insert into possessions values (NULL, 'Toastation', 6, '2019-02-16', 'OCCASION', '2019-04-19', 4, 96) ;
insert into possessions values (NULL, 'Toastation', 18, '2019-01-15', 'NEUF', NULL, NULL, 90) ;
insert into possessions values (NULL, 'Toastation', 9, '2019-02-03', 'OCCASION', '2019-11-28', -1, 40) ;
insert into possessions values (NULL, 'Toastation', 2, '2019-02-03', 'OCCASION', '2019-11-28', -1, 40) ;

insert into possessions values (NULL, 'Gouvernathor', 1, '2019-04-12', 'NEUF', NULL, NULL, 90) ;
insert into possessions values (NULL, 'Gouvernathor', 3, '2019-02-16', 'OCCASION', '2019-04-19', 4, 96) ;
insert into possessions values (NULL, 'Gouvernathor', 3, '2019-01-15', 'NEUF', NULL, NULL, 90) ;
insert into possessions values (NULL, 'Gouvernathor', 11, '2019-02-03', 'OCCASION', '2019-11-28', -1, 40) ;
insert into possessions values (NULL, 'Gouvernathor', 12, '2019-02-03', 'OCCASION', '2019-6-28', -1, 40) ;

-- decks

alter table decks AUTO_INCREMENT = 1;

insert into decks values (NULL, 'deck fort', 'Matodo') ; 
insert into decks values (NULL, 'deck nul', 'Matodo') ; 
insert into decks values (NULL, 'deck cool', 'Boytus') ; 
insert into decks values (NULL, 'deck X', 'Toastation') ; 
insert into decks values (NULL, 'deck Y', 'Gouvernathor') ; 

-- MEMBERSHIPS

insert into MEMBERSHIPS values (1, 1) ;
insert into MEMBERSHIPS values (5, 1) ;
insert into MEMBERSHIPS values (3, 2) ;
insert into MEMBERSHIPS values (7, 2) ;
insert into MEMBERSHIPS values (9, 3) ;
insert into MEMBERSHIPS values (10, 3) ;
insert into MEMBERSHIPS values (13, 4) ;
insert into MEMBERSHIPS values (14, 4) ;
insert into MEMBERSHIPS values (17, 5) ;
insert into MEMBERSHIPS values (18, 5) ;

-- games

alter table games AUTO_INCREMENT = 1;

insert into games values (NULL, '2019-01-02', 'Bordeaux', 'Foyer', 'Matodo') ;
insert into games values (NULL, '2019-01-03', 'Bordeaux', 'Foyer', 'Boytus') ;
insert into games values (NULL, '2019-01-04', 'Bordeaux', 'Magasin', 'Toastation') ;

-- plays

insert into plays values (1, 1, 'Matodo') ;
insert into plays values (1, 5, 'Gouvernathor') ;
insert into plays values (2, 2, 'Matodo') ;
insert into plays values (2, 3, 'Boytus') ;
insert into plays values (3, 1, 'Toastation') ;
insert into plays values (3, 4, 'Matodo') ;

-- -- ============================================================
-- --    verification des donnees
-- -- ============================================================

select count(*),'= 14 ?','CARDS' from CARDS 
union
select count(*),'= 19 ?','VERSIONS' from VERSIONS 
union 
select count(*),'= 4 ?','PLAYERS' from PLAYERS
union 
select count(*),'= 6 ?','PLAYS' from PLAYS
union 
select count(*),'= 3 ?','GAMES' from GAMES
union 
select count(*),'= 5 ?','DECKS' from DECKS
union 
select count(*),'= 21 ?','POSSESSIONS' from POSSESSIONS
union 
select count(*),'= 10 ?','MEMBERSHIPS' from MEMBERSHIPS
commit ; 
