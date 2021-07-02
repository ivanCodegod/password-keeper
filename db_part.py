import psycopg2
from config import config
from time import sleep
from tqdm import tqdm
from tabulate import tabulate


def help_note():
    print(f"\n-------------------------------------------------\n'get' - To get your information that you have "
          f"already save.\n'set' - To set your information into a storage.\n'all' - To see all Title's.\n'q' To quit "
          f"the program.\n'comm' - To see all available commands.\n-------------------------------------------------")


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
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        if not get and param == "get":  # get information
            title = input("Enter name of Title: ")
            cur.execute(f"SELECT title, login, pass, email from users_information where title = '{title}'")
            response = cur.fetchall()
            # Progress bar
            for i in tqdm(range(2)):
                sleep(1)

            print(f"\n{parsing(response)}" if response else f"\nThere is no such information like <<{title}>>")
            print("Write 'coom' To see all commands\nWrite 'q' to quit")
        elif not get and param == 'search_all':  # get all available title of information
            print("Searching all available Title's...\n")

            cur.execute(f"SELECT title from users_information order by title")
            response = cur.fetchall()
            # Progress bar
            for i in tqdm(range(2)):
                sleep(1)

            print(f"\n{parsing(response)}\n\nYou can open any of them." if response else f"\nThere is no title's, you "
                                                                                         f"can add one.")
            print("Write 'coom' To see all commands\nWrite 'q' to quit")
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
            print("Write 'coom' To see all commands\nWrite 'q' to quit")

            cur.executemany(sql, sql_list)
            conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def main():
    FLAG = True
    print(f"Welcome to <<Password keeper program>>\nIn this program you can store your passwords for easy or get it "
          f"back.\n\n")
    print(f"To see all commands write 'comm'\nIf you need to get info, print 'get'\nIf you need to set "
          "info, ""print 'set'\nTo see all titles of information write 'all'\nTo quit the program write 'q'\n\t\t")
    while FLAG:
        user = input("----->  ").lower()
        if user == 'all':
            process(False)
        elif user == 'get':
            process(False, "get")
        elif user == 'set':
            process(True, "")
        elif user == 'comm':
            help_note()
        elif user == 'q':
            print("Program stopped")
            FLAG = False


if __name__ == '__main__':
    main()
