import mysql.connector as mysql



def main():
    conn = mysql.connect(host='localhost',
                         user='root',
                         password='12345',
                         db='nadavdb1',
                         port=3306)
    cursor = conn.cursor()




if __name__ == '__main__':
    main()
