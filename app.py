
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
