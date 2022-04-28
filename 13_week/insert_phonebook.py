import psycopg2
import csv
from config import config

def insert_name_number(person_name, person_number):
    sql = "INSERT INTO PhoneBook(person_name, person_number) VALUES(%s,%s)"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (person_name, person_number))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

names = []         #an empty list to store the second column
numbers = []
with open(r'.\phoneBook.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
      tup = (row[0],)
      names.append(tup)
      tup = (row[1],)
      numbers.append(tup)

for x in range(0, len(names)):
    insert_name_number(names[x-1], numbers[x-1])
