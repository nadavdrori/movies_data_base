
import sqlite3

database = ""
conn = sqlite3.connect(database)
cursor = conn.cursor()

movies = f"CREATE TABLE Movies (id INTEGER NOT NULL" \
         f"                     name VARCHAR NOT NULL" \
         f"                     voteAvg DOUBLE NOT NULL" \
         f"                     budget INTEGER NOT NULL" \
         f"                     revenue INTEGER NOT NULL" \
         f"PRIMARY KEY (id)" \
         f"CHECK (voteAvg >= 0 and budget >= 0 and revenue >= 0)" \
         f"CREATE INDEX movie_name ON Movies(name);" \
         f");"

genre = f"CREATE TABLE Genre (id INTEGER NOT NULL" \
         f"                   name VARCHAR NOT NULL" \
         f"PRIMARY KEY (id)" \
         f");"

movie_genre = f"CREATE TABLE MovieGenre (movie_id INTEGER NOT NULL" \
              f"                          genre_id VARCHAR NOT NULL" \
              f"FOREIGN KEY (movie_id) REFERENCES Movies(id)" \
              f"FOREIGN KEY (genre_id) REFERENCES Genre(id)" \
              f");"

keywords = f"CREATE TABLE Keywords (id INTEGER NOT NULL" \
           f"                       word VARCHAR NOT NULL" \
           f"CREATE INDEX key_word ON Keywords(word);" \
           f"PRIMARY KEY (id)" \
           f");"

movie_keywords = f"CREATE TABLE MovieKeywords (movie_id INTEGER NOT NULL" \
                 f"                            word_id INTEGER NOT NULL" \
                 f"FOREIGN KEY (movie_id) REFERENCES Movies(id)" \
                 f"FOREIGN KEY (word_id) REFERENCES Keywords(id)" \
                 f");"

cursor.execute(movies)
cursor.execute(genre)
cursor.execute(movie_genre)
cursor.execute(keywords)
cursor.execute(movie_keywords)

result = cursor.fetchall()

conn.close()


