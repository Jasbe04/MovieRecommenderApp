import streamlit as st
import pickle
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Movie Recommender System")


if os.path.exists('movies_dict.pkl'):
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
else:
    st.error("movies_dict.pkl file not found.")
    st.stop()


if os.path.exists('similarity.pkl'):
    similarity = pickle.load(open('similarity.pkl', 'rb'))
else:
    st.info("Generating similarity matrix, please wait...")
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['description'].fillna(''))
    similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
    with open('similarity.pkl', 'wb') as f:
        pickle.dump(similarity, f)
    st.success("similarity.pkl generated successfully!")


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies


selected_movie = st.selectbox(
    'Choose your favorite movie:',
    movies["title"].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for movie in recommendations:
        st.write(movie)
