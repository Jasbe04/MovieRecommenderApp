
# import streamlit as st
# import pickle
# import numpy as np

# st.title("Movie Recommender System")


# movies_list = pickle.load(open('movies.pkl', 'rb')) 
# movies_list = movies_list['title'].values 
# similarity = pickle.load(open('similarity.pkl', 'rb')) 

# def recommend(movie):
    
#     movie_index = np.where(movies_list == movie)[0][0]
#     distances = similarity[movie_index]
#     movies_idx = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommended_movies = [movies_list[i[0]] for i in movies_idx]
#     return recommended_movies

# selected_movie_name = st.selectbox(
#     'Choose your favorite movie:',
#     movies_list
# )

# if st.button('Recommend'):
#     recommendations = recommend(selected_movie_name)
#     st.write("Recommended Movies:")
#     for i, movie in enumerate(recommendations, start=1):
#         st.write(f"{i}. {movie}")

# C:\Users\USER\OneDrive\Desktop\Code practice\Machine_Learning_Projects\Movies Recommender System  the current path

import streamlit as st
import pickle
import pandas as pd
st.title("Movie Recommender System")

# movies_list=pickle.load(open('movies.pkl','rb'))
# movies_list=movies_list['title'].values

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


selected_movies_name=st.selectbox(
    'Choose your favorite movie genre:',
    movies["title"].values
    # movies_list
    # ('Action', 'Comedy', 'Drama', 'Horror', 'Romance')
)

if st.button('Recommend'):
    recommendations=recommend(selected_movies_name)
    for i in recommendations:
        st.write(i)
    # st.write('You selected:', selected_movies_name)