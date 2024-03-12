import sqlite3

conn = sqlite3.connect(database)
cursor = conn.cursor()


def query_1(word):
    query = f"SELECT DISTINCT Movies.name AS movies with the keyword '{word}'" \
            f"FROM Keywords, MovieKeywords, Movies" \
            f"WHERE Keywords.word = '{word}' AND Keywords.id = MovieKeywords.word_id AND " \
            f"      MovieKeywords.movie_id = Movies.id"
    return query


def query_2(movie_name):
    query = f"SELECT Movies.name, Movies.voteAvg, Movies.budget, Movies.revenue, Genre.name, Keywords.word" \
            f"FROM Movies, Genre, MovieGenre, Keywords, MovieKeywords" \
            f"WHERE Movies.name = '{movie_name}' AND" \
            f"      Movies.id = MovieGenre.movie_id AND MovieGenre.genre_id = Genre.id AND " \
            f"      Movies.id = MovieKeywords.movie_id AND MovieKeywords.word_id = Keywords.id"
    return query


def query_3(genre, budget, revenue):
    query = f"SELECT Movies.name AS name, Movies.budget AS budget, Movies.revenue AS revenue," \
            f" (Movies.revenue-Movies.budget) AS profit" \
            f"FROM Movies, Genre, MovieGenre" \
            f"WHERE Movies.id IN = (SELECT Movies.id" \
            f"                      FROM Movies, Genre, MovieGenre" \
            f"                      WHERE Genre.name = '{genre}' AND MovieGenre.genre_id = Genre.id AND " \
            f"                            MovieGenre.movie_id = Movies.id) AND" \     
            f"      ORDER BY profit DESC"
    return query
