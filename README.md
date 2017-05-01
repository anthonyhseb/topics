# Titre du projet : 
Classement des documents par topic

## Contexte et objectifs du projet:
L’objectif du projet consiste à analyser les documents pour les classer dans différents topics. 
Nous allons procéder en deux étapes. Le première étape consiste à collectionner les documents à analyser. Ces documents sont les N meilleurs documents que le moteur de recherche google génère pour répondre à nos requêtes spécifiques. Dans deuxième étapes, nous classons ces documents dans différents topics. 

## Données (sources, quantité, évtl. pré-traitement, description):
### Phase de collection de données:
La source de nos données sont les résultats du moteur de recherche. Le processus consiste à établir une liste de requêtes spécifiques à envoyer au moteur de recherche. Pour chaque requête, nous garderons les N meilleurs documents générés par le moteur de recherche. dans cette étapes, le premier travail de "cleaninig" est réalisé pour enlever toutes les parties inutiles(ex: publicité). L'objectif est de générer une base de données avec la structure suivante : requête(passé au moteurde recherche), url du site, contenue de site

### Phase d'analyse de données :
La base, une fois créée, seront utilisée pour démarrer l'analyse. Dans cette phase, on va commencer par nettoyer les données non-déterminantes (ex: enlever le stopword, gestion de stemming, de lemmazation, de tokenization, etc.).


## Planification, répartition du travail:
Collection de données + traitement de données:Nirina
Analyse de données + traitement de données : kim

## Fonctionnalités / cas d’utilisation :


## Techniques, algorithmes et outils utilisés:
1. Partie de collection de données:
2. Partie d'analyse de données: Python distribution "Anacanda), language python, Tableaus software pour analyser les résultats.
3. Outil Jsoup: Librairie Java open source utilisée pour l'extraction et la manipulation des données dans des documents html.

## Conclusion:




