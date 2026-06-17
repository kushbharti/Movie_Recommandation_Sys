import ast
from nltk.stem.porter import PorterStemmer
from decouple import config
import requests



api_key = config('API_KEY')

ps = PorterStemmer()


# Converting string to list
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
       L.append(i['name'])
    return L
 
 
 # Converting string to list
def convert_cast(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
    return L
 
 # Taking director name
def fetch_director(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L


# Stemming
def stem(text):
    y = []
    
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"

        response = requests.get(
            url,
            timeout=15
        )

        if response.status_code != 200:
            print(f"TMDB Error: Status {response.status_code} for movie {movie_id}")
            return "https://via.placeholder.com/500x750?text=No+Poster"

        data = response.json()

        poster_path = data.get("poster_path")

        if not poster_path:
            print(f"No poster found for movie {movie_id}")
            return "https://via.placeholder.com/500x750?text=No+Poster"

        return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except requests.exceptions.RequestException as e:
        print(f"TMDB Error: {e}")
        return "https://via.placeholder.com/500x750?text=Error"
    
    
    