# Titre du projet : 
Classification des résultats d'un moteur de recherche

## Contexte et objectifs du projet:
L’objectif du projet consiste à analyser les pages web pour les classer dans différents thèmes. 
Nous allons procéder en deux étapes. La première étape consiste à collectionner les pages web. Ces dernières sont les N meilleurs résultats que le moteur de recherche google génère pour répondre à notre requête spécifique. Dans la deuxième étape, nous classons ces pages web dans les différents topics dont le nombre de thèmes peut est paramétré. 

## Données (sources, quantité, évtl. pré-traitement, description):
### Phase de collection de données:
La source de nos données sont les résultats du moteur de recherche. Le processus consiste à envoyer une requête au moteur de recherche et récupérer les N meilleurs pages web générées par le moteur de recherche pour les classer. Dans cette étape, le premier travail de "cleaninig" est réalisé pour enlever toutes les parties inutiles(ex: publicité, balises html). 

### Phase d'analyse de données :
les données (pages web) récupérées par la partie précédente, seront utilisées pour démarrer l'analyse. Dans cette phase, on va nettoyer ces données en appliquant les différents filtres : enlever le stopword, gestion de stemming, de lemmazation, de tokenization, etc.
Par la suite, nous appliquons l'alogorithme Latent Dirichlet Allocation (LDA) sur ces données nettoyées pour identifier les différentes thèmes.

#### Objectifs :
- 1.1 Identifier les thèmes (topics) ainsi que les termes associés
- 1.2 Classer les documents dans les thèmes identifiés
   
## Fonctionnalités / cas d’utilisation :
L'interface permet à nos utilisateurs finaux d'effectuer des recherches comme un moteur de recherche google. Cependant, au lieu de présenter une simple liste de documents, l'interface organise les résultats en les groupant sous différents thèmes.


## Planification, répartition du travail
1. Développement l'outil web scraping en Java (Nirina)
2. Implémentation initiale de l'algorithme LDA en python (Kim)
3. Conversion de l'outil web scraping de Java en python et améliorations (Anthony)
4. Développement d'un service REST fournissant les résultats d'analyse au client (Kim)
5. Implémentation de l'interface Web client (Nirina et Anthony)
6. Proposition d'un algorithme de nommage des thèmes, suite à une discussion avec les professeurs (Anthony)
7. Intégration et dernières améliorations (Nirina, Anthony, Kim)
 
## Techniques, algorithmes et outils utilisés:
1. Partie de collection de données: 
   1. Java-Jsoup: Librairie Java open source utilisée pour l'extraction et la manipulation des données dans des documents html. Cette version a été implémentée puis convertie en python. Ceci est dû au changement de language du projet en python.
   1. Nous avons développé l'outil googlesearch (Lien : https://github.com/anthonyhseb/googlesearch) en python (version finale utilisé dans le projet)
2. Partie d'analyse de données: 
   1. Librairie NLTK pour le pré-traitement des données
   2. librairie gensim.models.LdaModel pour analyser les données
3. Partie d'interface:
   1. Interface client web (HTML, CSS, JavaScript)
   2. Services REST (python Flask)

## Conclusion
Dans le cadre du projet, nous avons été amené à utiliser l'algorithme Latent Dirichlet Allocation (LDA) qui est l'algorithme standard dans le domaine de topic analysis. Nous avons rencontré des difficultés dans le nommage des thèmes, que LDA n'adresse pas. Ce problème reste toujours un sujet de recherche. Nous avons proposé un algorithme simple pour accorder à chaque thème un nom unique. 



