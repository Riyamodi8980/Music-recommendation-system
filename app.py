import streamlit as st
import pickle

movies_df = pickle.load(open('movies.pkl','rb'))
movies_list = movies_df["title"].values

st.title('Movie Recommender System')

similarity=pickle.load(open('simlarity.pkl','rb'))

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(enumerate(distances), reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies_df.iloc[i[0]]['title'])
    return recommended_movies

selected_movie_name = st.selectbox(
     'Select movie',
     (movies_list))

if st.button('Recommend'):
    movies = recommend(selected_movie_name)
    for i in movies:
        st.write(i)
