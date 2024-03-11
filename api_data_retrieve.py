import csv
import json
import sqlite3

CSV_FILE_NAME = 'tmdb_5000_movies.csv'
MOVIES_TABLE_NAME = 'Movies'
GENRES_TABLE_NAME = 'Genres'
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
    print(len(id_name_set))
    return list(id_name_set)


def insert_data_movies(cur):
    movie_tuples = get_tuples_by_columns(['id', 'title', 'vote_average', 'budget', 'revenue'])
    cur.executemany(f'INSERT INTO {MOVIES_TABLE_NAME} (id, name, voteAvg, budget, revenue) VALUES (?, ?, ?, ?, ?);',
                    movie_tuples)


def insert_data_genre(cur):
    all_genres = get_tuples_by_columns(['genres'])
    unique_genres_tuples = get_unique_id_name(all_genres)
    cur.executemany(f'INSERT INTO {GENRES_TABLE_NAME} (id, name) VALUES (?, ?);', unique_genres_tuples)


def insert_data_keyword(cur):
    all_keywords = get_tuples_by_columns(['keywords'])
    unique_keywords_tuples = get_unique_id_name(all_keywords)
    cur.executemany(f'INSERT INTO {MOVIE_KEYWORD_TABLE_NAME} (id, name) VALUES (?, ?);', unique_keywords_tuples)


def insert_data():
    conn = sqlite3.connect('db_server')  # change to 'sqlite:///your_filename.db'
    cur = conn.cursor()

    insert_data_movies(cur)
    insert_data_genre(cur)
    insert_data_keyword(cur)

    conn.commit()
    conn.close()


get_unique_id_name(get_tuples_by_columns(['keywords']))

# TODO: Implement insert MovieGenre and insert MovieKeyword
