def sanitize_input(user_input_list):
    for user_input in user_input_list:
        # sanitize user_input
        pass
    return


def query_1(keyword):
    sanitize_input([keyword])
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


def query_2(search_term):
    sanitize_input([search_term])
    """
    The following query retrieves all data associated with the movies that their title contains the search term.

    Parameters: search_term (str): The key to search for.
    Returns: str: SQL query string.
    """
    query = f"SELECT Movies.name, MAX(Movies.voteAvg), MAX(Movies.budget), MAX(Movies.revenue), GROUP_CONCAT(DISTINCT Genre.name SEPARATOR ', '), GROUP_CONCAT(DISTINCT Keywords.word SEPARATOR ', ') " \
            f"FROM Movies, Genre, MovieGenre, Keywords, MovieKeywords " \
            f"WHERE Movies.name LIKE '%{search_term}%' AND " \
            f"      Movies.id = MovieGenre.movie_id AND MovieGenre.genre_id = Genre.id AND " \
            f"      Movies.id = MovieKeywords.movie_id AND MovieKeywords.word_id = Keywords.id " \
            f" GROUP BY Movies.name"

    return query


def query_3(genre, profit):
    sanitize_input([genre, profit])
    """
    The following query retrieves all movies of the input genre with a profit equal or above the input profit.

    Parameters:
    genre (str): The name of the genre to filter movies by.
    profit (int): The desired profit margin.
    Returns: str: SQL query string.
    """

    query = f"SELECT DISTINCT Movies.name AS name, Movies.budget AS budget, Movies.revenue AS revenue," \
            f" Movies.profit " \
            f"FROM Movies, Genre, MovieGenre " \
            f"WHERE Movies.id IN (SELECT Movies.id " \
            f"                    FROM Movies, Genre, MovieGenre " \
            f"                    WHERE Genre.name = '{genre}' AND MovieGenre.genre_id = Genre.id AND " \
            f"                          MovieGenre.movie_id = Movies.id) AND " \
            f"                          Movies.profit >= '{profit}' " \
            f"      ORDER BY profit DESC"
    return query


def query_4(genre):
    sanitize_input([genre])
    """
    The following query calculates the average profit margin for movies from the input genre.

    Parameters: genre (str): The name of the genre to calculate the average profit margin for.
    Returns: str: SQL query string.
    """

    query = f"SELECT Genre.name AS genre, AVG(Movies.profit) AS profit " \
            f"FROM Movies, Genre, MovieGenre " \
            f"WHERE Genre.name = '{genre}' AND MovieGenre.genre_id = Genre.id AND MovieGenre.movie_id = Movies.id " \
            f"GROUP BY Genre.name " \
            f"ORDER BY profit"
    return query


def query_5(lower_budget, upper_budget):
    sanitize_input([lower_budget, upper_budget])
    """
    The following query returns the top genres of a movie for max audience satisfaction restrained to the input budget.
    """

    query = f"WITH movies_under_budget_constraint AS " \
            f"(SELECT id FROM Movies WHERE Movies.budget <= {upper_budget} AND Movies.budget > {lower_budget})" \
            f"SELECT Genre.name, avg(Movies.voteAvg) AS vote_avg " \
            f"FROM Movies, MovieGenre, Genre " \
            f"WHERE movie_id IN (SELECT id FROM movies_under_budget_constraint) " \
            f"AND Movies.id = MovieGenre.movie_id " \
            f"AND Genre.id = MovieGenre.genre_id " \
            f"GROUP BY Genre.name " \
            f"ORDER BY vote_avg DESC " \

    return query
