import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

def fetch_popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"

    response = requests.get(url)
    data = response.json()

    return data["results"]