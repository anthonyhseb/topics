# Titre du projet : 
Classement des documents par topic

## Contexte et objectifs du projet:
L’objectif du projet consiste à analyser les documents pour les classer dans différents topics. 
Nous allons procéder en deux étapes. Le première étape consiste à collectionner les documents à analyser. Ces documents sont les N meilleurs documents que le moteur de recherche google génère pour répondre à nos requêtes spécifiques. Dans deuxième étapes, nous classons ces documents dans différents topics. 

## Données (sources, quantité, évtl. pré-traitement, description):
### Phase de collection de données:
La source de nos données sont les résultats du moteur de recherche. Le processus consiste à établir une liste de requêtes spécifiques à envoyer au moteur de recherche. Pour chaque requête, nous garderons les N meilleurs documents générés par le moteur de recherche et les envoyer dans un fichier. Dans cette étapes, le premier travail de "cleaninig" est réalisé pour enlever toutes les parties inutiles(ex: publicité). L'objectif est de générer une base de données avec la structure suivante : requête(passé au moteurde recherche), url du site, contenue de site

### Phase d'analyse de données :
La base, une fois créée, seront utilisée pour démarrer l'analyse. Dans cette phase, on va commencer par nettoyer les données non-déterminantes (ex: enlever le stopword, gestion de stemming, de lemmazation, de tokenization, etc.).

#### Objectif 1: affiner les temrs par topic
- 1.1 Affiner le résultat en utilisant tf-idf au lieu de présence/absence du term
- 1.2 Reprendre les terms identifiés et re-requêter dans google

#### Objectif 2 : classer le nouveau document par topic (si le temps le permettre)

## Planification, répartition du travail:
1. Collection de données + traitement de données:Nirina
2. Analyse de données + traitement de données  : kim et anthony
         1. Objectif 1.1 => kim
         2. Objectif 1.2 => Anthony

## Fonctionnalités / cas d’utilisation :


## Techniques, algorithmes et outils utilisés:
1. Partie de collection de données: Nirina
         1. Outil Jsoup: Librairie Java open source utilisée pour l'extraction et la manipulation des données dans des documents html.
2. Partie d'analyse de données: 
         1. Python distribution "Anacanda", language python, Tableaus software pour analyser les résultats.


## Conclusion:




