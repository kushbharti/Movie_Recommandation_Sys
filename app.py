import streamlit as st
import pandas as pd
from model_train import recommend
import pickle

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
movies = movies.drop_duplicates(subset='title')


st.title("🎬 Movie Recommender System")


selected_movie_name = st.selectbox("How would you like to be contacted?", movies['title'].values)

if st.button("Search Movie"):
    names, posters = recommend(selected_movie_name)

    if names[0] == "Movie not found":
        st.error("Movie not found")
    else:
        cols = st.columns(5)

        for i in range(len(names)):
            with cols[i]:
                if posters[i]:
                    st.image(posters[i], width=200)

                st.write(names[i])
