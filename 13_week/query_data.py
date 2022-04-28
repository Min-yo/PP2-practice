from config import config
import psycopg2


conn = None
try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    #cur.execute('SELECT version()')
    cur.execute('''SELECT * FROM public.phonebook
    WHERE id = 3''')
    conn.commit()
    result = cur.fetchone()
    print(result)
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
