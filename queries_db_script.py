

def query_1(keyword):
    """
    The following query retrieves movies associated with the input keyword.

    Parameters: word (str): The keyword to search for.
    Returns: str: SQL query string.
    """

    query = f"SELECT DISTINCT Movies.name AS 'movies with the keyword {keyword}' " \
            f"FROM Keywords, MovieKeywords, Movies " \
            f"WHERE Keywords.word = '{keyword}' AND Keywords.id = MovieKeywords.word_id AND " \
            f"MovieKeywords.movie_id = Movies.id"
    return query


def query_2(movie_name):
    """
    The following query retrieves all data associated with the input movie.

    Parameters: movie_name (str): The name of the movie to search for.
    Returns: str: SQL query string.
    """
    query = f"SELECT Movies.name, MAX(Movies.voteAvg), MAX(Movies.budget), MAX(Movies.revenue), GROUP_CONCAT(DISTINCT Genre.name SEPARATOR ', '), GROUP_CONCAT(DISTINCT Keywords.word SEPARATOR ', ') " \
            f"FROM Movies, Genre, MovieGenre, Keywords, MovieKeywords " \
            f"WHERE Movies.name = '{movie_name}' AND " \
            f"      Movies.id = MovieGenre.movie_id AND MovieGenre.genre_id = Genre.id AND " \
            f"      Movies.id = MovieKeywords.movie_id AND MovieKeywords.word_id = Keywords.id " \
            f" GROUP BY Movies.name"

    return query


def query_3(genre, profit):
    """
    The following query retrieves movies of the input genre with a profit equal or above the input profit.

    Parameters:
    genre (str): The name of the genre to filter movies by.
    profit (int): The desired profit margin.
    Returns: str: SQL query string.
    """

    query = f"SELECT DISTINCT Movies.name AS name, Movies.budget AS budget, Movies.revenue AS revenue," \
            f" (Movies.revenue-Movies.budget) AS profit " \
            f"FROM Movies, Genre, MovieGenre " \
            f"WHERE Movies.id IN (SELECT Movies.id " \
            f"                    FROM Movies, Genre, MovieGenre " \
            f"                    WHERE Genre.name = '{genre}' AND MovieGenre.genre_id = Genre.id AND " \
            f"                          MovieGenre.movie_id = Movies.id) AND " \
            f"                          (Movies.revenue-Movies.budget) >= '{profit}' " \
            f"      ORDER BY profit DESC"
    return query


def query_4(genre):
    """
    The following query calculates the average profit margin for movies from the input genre.

    Parameters: genre (str): The name of the genre to calculate the average profit margin for.
    Returns: str: SQL query string.
    """

    query = f"SELECT Genre.name AS genre, AVG((Movies.revenue - Movies.budget)) AS profit" \
            f"FROM Movies, Genre, MovieGenre" \
            f"WHERE Genre.name = '{genre}' AND MovieGenre.genre_id = Genre.id AND MovieGenre.movie_id = Movies.id" \
            f"GROUP BY Genre.name"
    return query
