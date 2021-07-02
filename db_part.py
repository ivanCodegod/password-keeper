import psycopg2
from config import config
from time import sleep
from tqdm import tqdm


def process(out: bool, param=""):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        if not out:
            cur.execute(f"SELECT * from users_information where title = '{param}'")
            response = cur.fetchall()

            for i in tqdm(range(2)):
                sleep(1)

            print(f"\n{response}" if response else f"\nThere is no such information like <<{param}>>")
        else:
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
    user = input("If you need to get info, print <<get>>\nIf you need to get info, print <<set>>\n\t\t----->  ").lower()

    if user == 'get':
        process(False, input("Write 'Title' of your information, to get it: "))
    elif user == 'set':
        process(True, "")


if __name__ == '__main__':
    navigation()
