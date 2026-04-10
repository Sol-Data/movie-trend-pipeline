# Main execution code 

from src.extract.tmdb_api import fetch_popular_movies
from src.transform.transform_movies import transform_movies
from src.load.insert_movies import insert_movies
from src.load.create_table import create_table


def run_pipeline():
    print("Starting pipeline...")

    create_table()

    raw = fetch_popular_movies()
    df = transform_movies(raw)

    insert_movies(df)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()    