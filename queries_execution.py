import mysql.connector as mysql
import queries_db_script

# mysql -u nadavdrori -h mysqlsrv1.cs.tau.ac.il nadavdrori -p


def execute_print(cursor, query):
    cursor.execute(query)
    print('-------------------------')
    for row in cursor.fetchall():
        print(row)


def main():
    conn = mysql.connect(host='localhost',
                         user='root',
                         password='12345',
                         db='nadavdb1',
                         port=3306)
    cursor = conn.cursor()

    # example query no. 1
    '''execute_print(cursor, queries_db_script.query_1('elf'))
    execute_print(cursor, queries_db_script.query_1('magic'))
    execute_print(cursor, queries_db_script.query_1('fight'))
    execute_print(cursor, queries_db_script.query_1('prison'))
    execute_print(cursor, queries_db_script.query_1('hero'))
    execute_print(cursor, queries_db_script.query_1('family'))'''

    # example query no. 2
    '''execute_print(cursor, queries_db_script.query_2('The Matrix'))
    execute_print(cursor, queries_db_script.query_2('Avatar'))
    execute_print(cursor, queries_db_script.query_2('Forrest Gump'))'''

    # example query no. 3
    """execute_print(cursor, queries_db_script.query_3('horror', 100000000))
    execute_print(cursor, queries_db_script.query_3('comedy', 500000000))
    execute_print(cursor, queries_db_script.query_3('drama', 125000000))
    execute_print(cursor, queries_db_script.query_3('science fiction', 2000000000))"""

    # example query no. 4
    execute_print(cursor, queries_db_script.query_4('horror'))
    execute_print(cursor, queries_db_script.query_4('comedy'))
    execute_print(cursor, queries_db_script.query_4('drama'))
    execute_print(cursor, queries_db_script.query_4('science fiction'))


if __name__ == '__main__':
    main()
