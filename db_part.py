import psycopg2
from config import config
from time import sleep
from tqdm import tqdm
from tabulate import tabulate


def parsing(source):
    list_value = []
    column_list = ["title", "login", "password", "email"]

    for info in source:
        list_value.append(list(info))

    return tabulate(list_value, column_list, tablefmt="grid")


def process(get: bool, param="search_all"):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...\n')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        if not get and param != "search_all":  # get information
            cur.execute(f"SELECT title, login, pass, email from users_information where title = '{param}'")
            response = cur.fetchall()
            # Progress bar
            for i in tqdm(range(2)):
                sleep(1)

            print(f"\n{parsing(response)}" if response else f"\nThere is no such information like <<{param}>>")
        elif not get and param == 'search_all':  # get all available title of information
            print("Searching all available Title's...\n")

            cur.execute(f"SELECT title from users_information order by title")
            response = cur.fetchall()
            # Progress bar
            for i in tqdm(range(2)):
                sleep(1)

            print(f"\n{parsing(response)}\n\nYou can open any of them." if response else f"\nThere is no title's, you "
                                                                                         f"can add one.<<{param}>>")
        else:  # set information
            sql = f"insert into users_information (title,login,pass,email) values(%s,%s,%s,%s)"
            sql_list = [
                (input('Enter <<title>> of your info: '),
                 input('Enter <<login>>: '),
                 input('Enter <<password>>: '),
                 input('Enter <<email>>: '))
            ]
            # Progress bar
            for i in tqdm(range(3)):
                sleep(1)
            print('\nDone. Your information in safe!')

            cur.executemany(sql, sql_list)
            conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def navigation():
    print(f"Welcome to <<Password keeper program>>\nIn this program you can store your passwords for easy or get it "
          f"back.\n")
    user = input("If you need to get info, print <<get>>\nIf you need to set info, print <<set>>\n\t\t----->  ").lower()

    if user == 'get':
        process(False)
    elif user == 'set':
        process(True, "")


if __name__ == '__main__':
    navigation()
