# Creating a python database connection file

import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="moviesdb",
        user="admin",
        password="admin",
        port=5433
    )
    return conn
