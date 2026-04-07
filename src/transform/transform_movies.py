import pandas as pd

def transform_movies(raw_movies):
    movies = []

    for movie in raw_movies:
        movies.append({
            "id": movie["id"],
            "title": movie["title"],
            "release_date": movie["release_date"],
            "vote_average": movie["vote_average"],
            "popularity": movie["popularity"]
        })

    df = pd.DataFrame(movie)
    return df     