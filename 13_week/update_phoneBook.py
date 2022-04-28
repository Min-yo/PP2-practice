import psycopg2
from config import config


def update_name(id, person_name):
    sql = """ UPDATE PhoneBook
                SET person_name = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (person_name, id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def update_number(id, person_number):
    sql = """ UPDATE PhoneBook
                SET person_number = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (person_number, id))
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
    # Update person name id 1
    update_name(1, "Oliver")
    update_number(1, "+77013322476")