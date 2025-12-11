# Netflix Data Analysis & Visualization

Ce projet propose une analyse exploratoire du catalogue Netflix (films et séries) à l'aide de Python (Pandas, Matplotlib, Seaborn) et une application interactive Streamlit.

## Contenu du Projet

- **Projet_Netflix.ipynb** : Notebook Jupyter contenant l'analyse exploratoire des données (EDA), le nettoyage, et des visualisations avancées (corrélations, tendances temporelles, nuages de mots, etc.).
- **app.py** : Application Streamlit offrant un tableau de bord interactif pour explorer les données.
- **netflix_titles.csv** : Le jeu de données utilisé (source : Kaggle).
- **report_content.md** : Synthèse des observations et conclusions.

## Installation

1.  Cloner ce dépôt :
    ```bash
    git clone <votre-repo-url>
    cd <dossier-du-projet>
    ```

2.  Installer les dépendances :
    ```bash
    pip install pandas numpy matplotlib seaborn plotly streamlit jupyter wordcloud
    ```

## Utilisation

### Lancer le Notebook
Ouvrez le notebook dans Jupyter Lab ou VS Code :
```bash
jupyter notebook Projet_Netflix.ipynb
```
Exécutez toutes les cellules pour voir l'analyse complète.

### Lancer l'application Streamlit
Exécutez la commande suivante dans votre terminal :
```bash
streamlit run app.py
```
L'application s'ouvrira dans votre navigateur par défaut (généralement à l'adresse `http://localhost:8501`).

Une version deployé existe aussi ( `https://8pro408--mini-projet.streamlit.app/` ) 

[Le StreamLint](https://8pro408--mini-projet.streamlit.app/)

## Fonctionnalités de l'application
- **Filtres** : Filtrez par type (Film/Série), pays et année d'ajout.
- **KPIs** : Visualisez rapidement le nombre total de titres.
- **Graphiques Interactifs** : Explorez la répartition des genres, l'évolution temporelle et la distribution géographique.
- **Données** : Accédez aux données brutes filtrées.





