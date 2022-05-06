#!/usr/bin/python
import psycopg2
from config import config


def get_numbers():
    """ get numbers provided by a part of a name """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # another way to call a function
        # cur.execute("SELECT * FROM get_numbers_by_names( %s); ",(id,))
        cur.callproc('get_numbers_by_names')
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_numbers()