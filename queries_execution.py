

import mysql.connector as mysql
import queries_db_script

# mysql -u nadavdrori -h mysqlsrv1.cs.tau.ac.il nadavdrori -p

def main():
    conn = mysql.connect(host='localhost',
                         user='root',
                         password='12345',
                         db='nadavdb1',
                         port=3306)
    cursor = conn.cursor()

    # example query no. 1
    cursor.execute(queries_db_script.query_1('elf'))
    cursor.execute(queries_db_script.query_1('magic'))
    cursor.execute(queries_db_script.query_1('fight'))
    cursor.execute(queries_db_script.query_1('prison'))
    cursor.execute(queries_db_script.query_1('hero'))
    cursor.execute(queries_db_script.query_1('family'))

    # example query no. 2
    #cursor.execute(queries_db_script.query_2('The Matrix'))
    """cursor.execute(queries_db_script.query_2('Avatar'))
    cursor.execute(queries_db_script.query_2('The Hobbit'))"""

    # example query no. 3
    #cursor.execute(queries_db_script.query_3('horror', 100000000))
    """cursor.execute(queries_db_script.query_3('comedy', 500000000))
    cursor.execute(queries_db_script.query_3('drama', 125000000))
    cursor.execute(queries_db_script.query_3('science fiction', 1000000000))"""

    # example query no. 4
    #cursor.execute(queries_db_script.query_4('horror'))
    """cursor.execute(queries_db_script.query_4('comedy'))
    cursor.execute(queries_db_script.query_4('drama'))
    cursor.execute(queries_db_script.query_4('science fiction'))"""




if __name__ == '__main__':
    main()
