
import mysql.connector as mysql


conn = mysql.connect(host='localhost',
                     user='root',
                     password='12345',
                     db='nadavdb1',
                     port=3306)
cursor = conn.cursor()

movies = f"CREATE TABLE Movies (id INTEGER NOT NULL," \
         f"                     name VARCHAR (100) NOT NULL UNIQUE," \
         f"                     voteAvg DOUBLE NOT NULL," \
         f"                     budget INTEGER NOT NULL," \
         f"                     revenue INTEGER NOT NULL," \
         f"PRIMARY KEY (id)," \
         f"CHECK (voteAvg >= 0 and budget >= 0 and revenue >= 0)," \
         f");" \
         f"CREATE INDEX movie_name ON Movies(name);"

genre = f"CREATE TABLE Genre (id INTEGER NOT NULL," \
         f"                   name VARCHAR (100) NOT NULL UNIQUE," \
         f"PRIMARY KEY (id)" \
         f");"

movie_genre = f"CREATE TABLE MovieGenre (movie_id INTEGER NOT NULL," \
              f"                         genre_id VARCHAR (100) NOT NULL," \
              f"FOREIGN KEY (movie_id) REFERENCES Movies(id)," \
              f"FOREIGN KEY (genre_id) REFERENCES Genre(id)" \
              f");"

keywords = f"CREATE TABLE Keywords (id INTEGER NOT NULL," \
           f"                       word VARCHAR (100) NOT NULL UNIQUE," \
           f"PRIMARY KEY (id)" \
           f");" \
           f"CREATE INDEX key_word ON Keywords(word);"

movie_keywords = f"CREATE TABLE MovieKeywords (movie_id INTEGER NOT NULL" \
                 f"                            word_id INTEGER NOT NULL" \
                 f"FOREIGN KEY (movie_id) REFERENCES Movies(id)" \
                 f"FOREIGN KEY (word_id) REFERENCES Keywords(id)" \
                 f");"

cursor.execute(movies, multi=True)
cursor.execute(genre)

"""rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.execute(movie_genre)
cursor.execute(keywords, multi=True)
cursor.execute(movie_keywords)"""


cursor.close()
conn.close()


