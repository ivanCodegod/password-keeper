import psycopg2
from config import config
from tabulate import tabulate
from db_addition import help_list, progress_bar


def parsing(source):
    list_value = []
    column_list = ["title", "login", "password", "email"]

    for info in source:
        list_value.append(list(info))

    return tabulate(list_value, column_list, tablefmt="grid")


def process(way_of_processing: str):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        if way_of_processing == "get":  # get information for a given 'title'
            title = input("Enter name of Title: ")
            cur.execute(f"SELECT title, login, pass, email from users_information where title = '{title}'")
            response = cur.fetchall()

            progress_bar()
            print(f"\n{parsing(response)}\n{help_list['help_propose']}" if response else f"\nThere is no such "
                  f"information like <<{title}>>\n{help_list['help_propose']}")

        elif way_of_processing == 'all':  # get all available title of information
            print("Searching all available Note's...")

            cur.execute(f"SELECT title from users_information order by title")
            response = cur.fetchall()

            progress_bar()
            print(f"\n{parsing(response)}\n{help_list['help_propose']}" if response else f"\nThere is no "
                  f"title's, you can add one.")
        elif way_of_processing == 'set':  # set information
            sql = f"insert into users_information (title,login,pass,email) values(%s,%s,%s,%s)"
            sql_list = [
                (input('Enter <<title>> of your info: '),
                 input('Enter <<login>>: '),
                 input('Enter <<password>>: '),
                 input('Enter <<email>>: '))
            ]

            progress_bar()
            print(f"\nDone! Your information is save.\n{help_list['help_propose']}")

            cur.executemany(sql, sql_list)
            conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def main():
    flag = True
    print(help_list['intro'])
    print(help_list['commands'])

    while flag:
        user = input("----->  ").lower()
        if user == 'all':
            process('all')
        elif user == 'get':
            process('get')
        elif user == 'set':
            process('set')
        elif user == 'comm':
            print(help_list['commands'])
        elif user == 'q':
            print("Program stopped")
            flag = False
        else:
            print(f"No such commands like: {user}\n{help_list['commands']}")


if __name__ == '__main__':
    main()
