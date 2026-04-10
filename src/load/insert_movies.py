# Add INSERT code

from src.load.db import get_connection

def insert_movies(df):
    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO movies (id, title, release_date, vote_average, popularity)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (
            row["id"],
            row["title"],
            row["release_date"],
            row["vote_average"],
            row["popularity"]
        ))

    conn.commit()
    cur.close()
    conn.close()
        