def create_db(conn):
    cursor = conn.cursor()

    movies = f"CREATE TABLE Movies (id INTEGER NOT NULL," \
             f"                     name VARCHAR (100) NOT NULL," \
             f"                     voteAvg REAL NOT NULL," \
             f"                     budget BIGINT NOT NULL," \
             f"                     revenue BIGINT NOT NULL," \
             f"                     profit BIGINT AS (revenue - budget), " \
             f"PRIMARY KEY (id)" \
             f");"

    """ 
    This line creates an index on the 'name' column of the 'Movies' table,
    we did that in order to search for movies by name efficiently
    
    """
    movies_index = f"CREATE FULLTEXT INDEX movie_name ON Movies(name);"

    movies_profit_index = f"CREATE INDEX movie_profit ON Movies(profit);"

    movies_budget_index = f"CREATE INDEX movie_budget ON Movies(budget);"

    genre = f"CREATE TABLE Genre (id INTEGER NOT NULL," \
             f"                   name VARCHAR (100) NOT NULL UNIQUE," \
             f"PRIMARY KEY (id)" \
             f");"

    movie_genre = f"CREATE TABLE MovieGenre (movie_id INTEGER NOT NULL," \
                  f"                         genre_id INTEGER NOT NULL," \
                  f"FOREIGN KEY (movie_id) REFERENCES Movies(id)," \
                  f"FOREIGN KEY (genre_id) REFERENCES Genre(id)" \
                  f");"

    keywords = f"CREATE TABLE Keywords (id INTEGER NOT NULL," \
               f"                       word VARCHAR (100) NOT NULL," \
               f"PRIMARY KEY (id)" \
               f");"

    """ 
    This part creates an index on the 'word' column of the 'Keywords' table,
    we did that in order to search efficiently for words associated with certain movies 
    """
    keywords_index = f"CREATE FULLTEXT INDEX key_word ON Keywords(word);"

    movie_keywords = f"CREATE TABLE MovieKeywords (movie_id INTEGER NOT NULL," \
                     f"                            word_id INTEGER NOT NULL," \
                     f"FOREIGN KEY (movie_id) REFERENCES Movies(id)," \
                     f"FOREIGN KEY (word_id) REFERENCES Keywords(id)" \
                     f");"

    cursor.execute(movies)
    cursor.execute(movies_index)
    cursor.execute(movies_profit_index)
    cursor.execute(movies_budget_index)
    cursor.execute(genre)
    cursor.execute(movie_genre)
    cursor.execute(keywords)
    cursor.execute(keywords_index)
    cursor.execute(movie_keywords)

    cursor.close()


def clean_db(conn):
    cursor = conn.cursor()
    clean_cmd = 'DROP TABLE MovieKeywords; DROP TABLE MovieGenre; DROP TABLE Movies; DROP TABLE Genre; DROP TABLE Keywords;'
    cursor.execute(clean_cmd)
    cursor.close()
