# INSTALLATION

## Dépendances python :

* ```pip install pymysql```
* ```pip install yaml```

## Configuration 
Renommer le fichier ```.env.dist``` en ```.env``` et le compléter.

# Utilisation

Lancer ```make shell``` pour lancer le shell.
Utiliser la commande help pour avoir la liste des commandes ou se référer à la partie suivante.


## Liste des commandes

* add [card|player|...] : lance un formulaire pour l'ajout de valeur dans la table spécifiée
* remove [card|player|...] : lance un formulaire pour la suppression d'une valeur dans la table spécifiée
* list [cards|players|...] : affiche l'ensemble des valeurs de la table spécifié
* consult [arg] : lance la consultation donnée en paramètre (appuyer sur TAB pour l'autocomplétion)
* statistics [arg] : lance la commande de statistique donnée en paramètre (appuyer sur TAB pour l'autocomplétion)
* populate fichier.sql [fichier2.sql ...] : lance les commandes sql dans les fichiers donnés en paramètre

Liste des consultations :
* cards_by_type
* cards_in_possession
* cards_not_in_deck
* players_collectors 

Liste des statistiques : 
* player_nb_cards
* players_by_value
* cards_in_decks
* player_rare_collectors
* cards_familly