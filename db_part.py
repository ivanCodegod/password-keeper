#!/usr/bin/python
import psycopg2
from config import config


def connect(param):
    """ Connect to the PostgreSQL database server """
    global db_version
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        # print('PostgreSQL database version:')
        cur.execute(f"SELECT * from users_information where title = '{param}'")

        # display the PostgreSQL database server version
        db_version = cur.fetchall()

        print(f"{db_version}")

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return db_version


def navigation():
    print(
        f"Welcome to <<Password keeper program>>\nIn this program you can store your passwords for easy or get it back.\n")
    user = input("If you need to get info, print <<get>>\nIf you need to get info, print <<set>>\n\t\t----->  ").lower()

    if user == 'get':
        connect(input("Write 'Title' of your information, to get it: "))
    elif user == 'set':
        ...


if __name__ == '__main__':
    navigation()
