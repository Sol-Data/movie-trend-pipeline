from src.extract.tmdb_api import fetch_popular_movies
from src.transform.transform_movies import transform_movies

def run_pipeline():
    raw = fetch_popular_movies()
    df = transform_movies(raw)

    print(df.head())

if __name__ == "__main__":
    run_pipeline()    