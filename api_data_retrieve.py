import csv
import json
import mysql.connector as mysql

CSV_FILE_NAME = 'tmdb_5000_movies.csv'
MOVIES_TABLE_NAME = 'Movies'
GENRES_TABLE_NAME = 'Genres'
KEYWORDS_TABLE_NAME = 'Keywords'
MOVIE_GENRE_TABLE_NAME = 'MovieGenre'
MOVIE_KEYWORD_TABLE_NAME = 'MovieKeyword'


def get_tuples_by_columns(column_list):
    tuples = []

    with open(CSV_FILE_NAME, 'r') as file:
        file_reader = csv.DictReader(file)  # Comma is default delimiter
        for row in file_reader:
            row_to_insert = []
            for i in range(len(column_list)):
                row_to_insert.append(row[column_list[i]])
            tuples.append(tuple(row_to_insert))

    return tuples


def get_unique_id_name(row_tuples):
    id_name_set = set()
    for row_tuple in row_tuples:
        json_id_name_list = json.loads(row_tuple[0])  # Access the first and only object of each tuple
        for json_id_name in json_id_name_list:  # Iterate through the (id, name) objects
            id_name_set.add((json_id_name['id'], json_id_name['name']))

    return list(id_name_set)


def validate_unique_id(tuples, table):  # Validate uniqueness of primary key values
    id_set = set()
    for id_value_tuple in tuples:
        if id_value_tuple[0] in id_set:
            raise f'Non unique id found {id_value_tuple[0]} in {table}'
        id_set.add(id_value_tuple[0])


def populate_movies(cur=None):
    movie_tuples = get_tuples_by_columns(['id', 'title', 'vote_average', 'budget', 'revenue'])
    validate_unique_id(movie_tuples, 'movies')
    if cur:
        cur.executemany(
            f'INSERT INTO {MOVIES_TABLE_NAME} (id, name, voteAvg, budget, revenue) VALUES (%d, %s, %f, %d, %d);',
            movie_tuples)

    print(f'Inserting {len(movie_tuples)} rows to {MOVIES_TABLE_NAME}')

    return movie_tuples


def populate_genre(cur=None):
    all_genres = get_tuples_by_columns(['genres'])
    unique_genres_tuples = get_unique_id_name(all_genres)
    validate_unique_id(unique_genres_tuples, 'genres')
    if cur:
        cur.executemany(f'INSERT INTO {GENRES_TABLE_NAME} (id, name) VALUES (%d, %s);', unique_genres_tuples)

    print(f'Inserting {len(unique_genres_tuples)} rows to {GENRES_TABLE_NAME}')

    return unique_genres_tuples


def populate_keyword(cur=None):
    all_keywords = get_tuples_by_columns(['keywords'])
    unique_keywords_tuples = get_unique_id_name(all_keywords)
    validate_unique_id(unique_keywords_tuples, 'keywords')

    if cur:
        cur.executemany(f'INSERT INTO {KEYWORDS_TABLE_NAME} (id, name) VALUES (%d, %s);', unique_keywords_tuples)

    print(f'Inserting {len(unique_keywords_tuples)} rows to {MOVIE_KEYWORD_TABLE_NAME}')

    return unique_keywords_tuples


def populate_movie_genre(cur=None):
    movie_id_movie_genre = get_tuples_by_columns(['id', 'genres'])
    movie_id_genre_id_tuples = []

    for movie_id_movie_genre_row in movie_id_movie_genre:
        movie_id = movie_id_movie_genre_row[0]  # Access movie id of the tuple
        json_genre_list = json.loads(movie_id_movie_genre_row[1])  # Access genre list of the tuple

        for json_genre_id_name in json_genre_list:  # Iterate through the (id, name) objects
            movie_id_genre_id_tuples.append((int(movie_id), json_genre_id_name['id']))

    if cur:
        cur.executemany(f'INSERT INTO {MOVIE_GENRE_TABLE_NAME} (id, name) VALUES (%d, %s);', movie_id_genre_id_tuples)

    print(f'Inserting {len(movie_id_genre_id_tuples)} rows to {MOVIE_GENRE_TABLE_NAME}')

    return movie_id_genre_id_tuples


def populate_movie_keyword(cur=None):
    movie_id_movie_keyword = get_tuples_by_columns(['id', 'keywords'])
    movie_id_keyword_id_tuples = []

    for movie_id_movie_keyword_row in movie_id_movie_keyword:
        movie_id = movie_id_movie_keyword_row[0]  # Access movie id of the tuple
        json_keyword_list = json.loads(movie_id_movie_keyword_row[1])  # Access genre list of the tuple

        for json_keyword_id_name in json_keyword_list:  # Iterate through the (id, name) objects
            movie_id_keyword_id_tuples.append((int(movie_id), json_keyword_id_name['id']))

    if cur:
        cur.executemany(f'INSERT INTO {MOVIE_KEYWORD_TABLE_NAME} (id, name) VALUES (%d, %s);',
                        movie_id_keyword_id_tuples)

    print(f'Inserting {len(movie_id_keyword_id_tuples)} rows to {MOVIE_KEYWORD_TABLE_NAME}')

    return movie_id_keyword_id_tuples


def insert_data():
    conn = mysql.connect(host='localhost',
                         user='root',
                         password='12345',
                         db='nadavdb1',
                         port=3306)
    cur = conn.cursor()

    print(populate_movies(cur)[:3])
    print(populate_genre(cur)[:3])
    print(populate_keyword(cur)[:3])
    print(populate_movie_genre(cur)[:3])
    print(populate_movie_keyword(cur)[:3])

    cur.close()
    conn.close()


insert_data()
