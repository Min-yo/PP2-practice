import psycopg2
from config import config


def delete_number(person_name):
    sql = """ DELETE FROM PhoneBook WHERE person_name = '{}'""".format(person_name)
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows



if __name__ == '__main__':
    delete_number("John")