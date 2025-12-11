# Rapport d'Analyse du Catalogue Netflix

## 1. Introduction
Ce rapport présente les résultats de l'analyse exploratoire menée sur le dataset Netflix, comprenant 8 807 titres. L'objectif était de comprendre la composition du catalogue, sa diversité et ses évolutions.

## 2. Structure et Qualité des Données
Le dataset contient des informations sur les titres, réalisateurs, acteurs, pays, dates d'ajout, années de sortie, classifications et durées.
- **Valeurs manquantes** : Principalement dans les colonnes `director`, `cast` et `country`.
- **Nettoyage** : La colonne `date_added` a été convertie en format date, et une colonne `main_country` a été créée pour simplifier l'analyse géographique.

## 3. Analyse des Contenus
- **Films vs Séries** : Le catalogue est dominé par les films (~70%), bien que la part des séries soit significative.
- **Genres** : Les catégories "International Movies", "Dramas" et "Comedies" sont les plus représentées, indiquant une offre généraliste et internationale.
- **Géographie** : Les États-Unis sont le premier producteur, suivis par l'Inde et le Royaume-Uni.

## 4. Analyse Temporelle
- **Ajouts par année** : On observe une croissance constante du nombre de contenus ajoutés jusqu'en 2019, suivie d'un ralentissement (probablement lié à la pandémie et à la saturation du marché).
- **Année de sortie** : Le catalogue se concentre sur des contenus récents, la majorité des titres datant des 10 dernières années.

## 5. Tendances et Corrélations
- **Genres par Pays** : L'analyse des corrélations montre des spécialisations (ex: beaucoup de "Dramas" en Inde et Corée du Sud).
- **Durée** : La durée moyenne des films se situe autour de 90-100 minutes.

## 6. Conclusion
Netflix propose un catalogue riche et diversifié, avec une forte empreinte internationale. L'outil de visualisation interactif (Streamlit) permet d'explorer ces tendances en détail selon les préférences de l'utilisateur.
