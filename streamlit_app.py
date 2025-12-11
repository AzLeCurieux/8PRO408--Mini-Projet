import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.set_page_config(page_title="Netflix Data Analysis", layout="wide")

st.title("Netflix Data Analysis Dashboard")
st.markdown("Explorez le catalogue Netflix : Films, Séries, Genres, et plus encore.")

@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['main_country'] = df['country'].str.split(',').str[0]
    df['duration_min'] = df['duration'].astype(str).str.replace(' min', '', regex=False)
    df['duration_min'] = pd.to_numeric(df['duration_min'], errors='coerce')
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Le fichier 'netflix_titles.csv' est introuvable. Veuillez le télécharger.")
    st.stop()

st.sidebar.header("Filtres")
selected_type = st.sidebar.multiselect("Type de contenu", df['type'].unique(), default=df['type'].unique())
selected_country = st.sidebar.multiselect("Pays principal", df['main_country'].dropna().unique())
selected_year = st.sidebar.slider("Année d'ajout", int(df['year_added'].min()), int(df['year_added'].max()), (2010, 2021))

filtered_df = df[
    (df['type'].isin(selected_type)) &
    (df['year_added'] >= selected_year[0]) &
    (df['year_added'] <= selected_year[1])
]

if selected_country:
    filtered_df = filtered_df[filtered_df['main_country'].isin(selected_country)]

col1, col2, col3 = st.columns(3)
col1.metric("Total Titres", len(filtered_df))
col2.metric("Films", len(filtered_df[filtered_df['type'] == 'Movie']))
col3.metric("Séries TV", len(filtered_df[filtered_df['type'] == 'TV Show']))


st.subheader("Répartition Films vs Séries")
fig_type = px.pie(filtered_df, names='type', title='Proportion des types de contenus', color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig_type, use_container_width=True)

st.subheader("Évolution du contenu ajouté par année")
content_by_year = filtered_df.groupby(['year_added', 'type']).size().reset_index(name='count')
fig_year = px.line(content_by_year, x='year_added', y='count', color='type', title="Nombre de titres ajoutés par an", markers=True)
st.plotly_chart(fig_year, use_container_width=True)

st.subheader("Top 10 Genres")
genres_df = filtered_df[['listed_in']].dropna()
genres_df['listed_in'] = genres_df['listed_in'].str.split(', ')
genres_exploded = genres_df.explode('listed_in')
top_genres = genres_exploded['listed_in'].value_counts().head(10).reset_index()
top_genres.columns = ['Genre', 'Count']

fig_genre = px.bar(top_genres, x='Count', y='Genre', orientation='h', title="Top 10 Genres les plus populaires", color='Count', color_continuous_scale='Viridis')
fig_genre.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig_genre, use_container_width=True)

st.subheader("Top 10 Pays Producteurs")
top_countries = filtered_df['main_country'].value_counts().head(10).reset_index()
top_countries.columns = ['Pays', 'Nombre de titres']
fig_country = px.bar(top_countries, x='Pays', y='Nombre de titres', title="Top 10 Pays", color='Nombre de titres')
st.plotly_chart(fig_country, use_container_width=True)

st.subheader("Distribution des Classifications (Ratings)")
rating_counts = filtered_df['rating'].value_counts().reset_index()
rating_counts.columns = ['Rating', 'Count']
rating_counts = rating_counts[rating_counts['Count'] > 0] 

fig_rating = px.bar(rating_counts, x='Rating', y='Count', title="Distribution des Ratings", color='Count')
st.plotly_chart(fig_rating, use_container_width=True)

st.subheader("Heatmap : Genres vs Top 10 Pays")
if not genres_exploded.empty and not filtered_df.empty:
    df_heatmap = filtered_df[['main_country', 'listed_in']].dropna()
    df_heatmap['listed_in'] = df_heatmap['listed_in'].str.split(', ')
    df_heatmap_exploded = df_heatmap.explode('listed_in')
    
    top_10_countries = df_heatmap_exploded['main_country'].value_counts().head(10).index
    top_10_genres = df_heatmap_exploded['listed_in'].value_counts().head(10).index
    
    df_heatmap_filtered = df_heatmap_exploded[
        df_heatmap_exploded['main_country'].isin(top_10_countries) & 
        df_heatmap_exploded['listed_in'].isin(top_10_genres)
    ]
    
    pivot_table = pd.crosstab(df_heatmap_filtered['listed_in'], df_heatmap_filtered['main_country'])
    
    fig_heatmap = plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
    st.pyplot(fig_heatmap)

st.subheader("Distribution de la durée des Films")
movies_only = filtered_df[filtered_df['type'] == 'Movie']
if not movies_only.empty:
    fig_duration = px.histogram(movies_only, x='duration_min', nbins=30, title="Distribution de la durée (minutes)", color_discrete_sequence=['skyblue'])
    st.plotly_chart(fig_duration, use_container_width=True)

st.subheader("Nuage de mots : Casting et Réalisateurs")
text_data = pd.concat([filtered_df['director'], filtered_df['cast']]).dropna().str.cat(sep=' ')
if text_data:
    wordcloud = WordCloud(width=800, height=400, background_color='black', colormap='Pastel1').generate(text_data)
    fig_wc, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig_wc)
else:
    st.info("Pas assez de données pour générer le nuage de mots.")


st.subheader("Données Brutes")
st.dataframe(filtered_df)

# Footer
st.markdown("---")
st.markdown("Réalisé avec Streamlit et Plotly")
