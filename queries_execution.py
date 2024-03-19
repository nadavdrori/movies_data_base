import mysql.connector as mysql
import api_data_retrieve
import create_db_script
import queries_db_script


def execute_print(cursor, query):
    try:
        cursor.execute(query)
        print('-------------------------')
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print(f'Failed to run query: {query}\nError msg: {e}')


def main():
    conn = mysql.connect(host='localhost',
                         user='nadavdrori',
                         password='nadavdror61892',
                         db='nadavdrori',
                         port=3305)

    # Clean DB - in case this script is being called when the DB is already set.
    '''try:
        create_db_script.clean_db(conn)
    except:
        pass'''

    # DB creation
    try:
        create_db_script.create_db(conn)
    except Exception as e:
        print(f'Failed to build DB\nError msg: {e}')

    # DB population
    try:
        api_data_retrieve.populate_db(conn)
    except Exception as e:
        print(f'Failed to populate DB\nError msg: {e}')

    # Execution examples
    cursor = conn.cursor()

    # example query no. 1
    execute_print(cursor, queries_db_script.query_1('elf'))
    execute_print(cursor, queries_db_script.query_1('magic'))
    execute_print(cursor, queries_db_script.query_1('fight'))
    execute_print(cursor, queries_db_script.query_1('prison'))
    execute_print(cursor, queries_db_script.query_1('hero'))
    execute_print(cursor, queries_db_script.query_1('family'))

    # example query no. 2
    execute_print(cursor, queries_db_script.query_2('The Matrix'))
    execute_print(cursor, queries_db_script.query_2('Avatar'))
    execute_print(cursor, queries_db_script.query_2('Forrest Gump'))

    # example query no. 3
    execute_print(cursor, queries_db_script.query_3('horror', 100000000))
    execute_print(cursor, queries_db_script.query_3('comedy', 500000000))
    execute_print(cursor, queries_db_script.query_3('drama', 125000000))
    execute_print(cursor, queries_db_script.query_3('science fiction', 2000000000))

    # example query no. 4
    execute_print(cursor, queries_db_script.query_4('horror'))
    execute_print(cursor, queries_db_script.query_4('comedy'))
    execute_print(cursor, queries_db_script.query_4('drama'))
    execute_print(cursor, queries_db_script.query_4('science fiction'))

    # example query no. 5
    execute_print(cursor, queries_db_script.query_5(0, 1000000000000000))  # "Unlimited" budget
    execute_print(cursor, queries_db_script.query_5(80000, 120000))  # Low budget
    execute_print(cursor, queries_db_script.query_5(0, 5000000))  # Up to 'X' budget


if __name__ == '__main__':
    main()
