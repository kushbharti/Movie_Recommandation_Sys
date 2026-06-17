# Importing the modules
import pandas as pd
from utils import convert,convert_cast,fetch_director,stem, fetch_poster
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time

# Reading the dataset
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merging the datasets
movies = movies.merge(credits,on='title')

# Selecting the required columns
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

# Droping missing values
movies.dropna(inplace=True)

# convert object to list
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert_cast)
movies['crew'] = movies['crew'].apply(fetch_director)
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Converting string to list
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ","") for i in x])

# Merging all the columns --> tags
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# New dataframe
new_df = movies[['movie_id','title','tags']].copy()

# Converting list to string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Converting to lowercase
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

# Stemming the tags
new_df['tags'] = new_df['tags'].apply(stem)

# TF-IDF vectorizer
tfidf = TfidfVectorizer(max_features=5000,stop_words='english')
vectors = tfidf.fit_transform(new_df['tags']).toarray()
similarity = cosine_similarity(vectors)

# Recommending the movies
def recommend(movie):
    try:
        movie_index = new_df[new_df['title'] == movie].index[0]

        distances = similarity[movie_index]

        movie_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        movies_suggested = []
        recommended_movies_posters = []

        for i in movie_list:
            movie_id = new_df.iloc[i[0]].movie_id

            print(f"Fetching: {new_df.iloc[i[0]].title}")
            print(f"Movie ID: {movie_id}")

            movies_suggested.append(
                new_df.iloc[i[0]].title
            )

            recommended_movies_posters.append(
                fetch_poster(movie_id)
            )

            time.sleep(0.5)

        return movies_suggested, recommended_movies_posters

    except Exception as e:
        print("Recommendation Error:", e)
        return ["Movie not found"], [""]
