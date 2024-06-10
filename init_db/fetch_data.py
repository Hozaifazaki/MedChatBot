import sqlite3

conn = sqlite3.connect('people.db')
cur = conn.cursor()

cmd = "SELECT * FROM person"

cur.execute(cmd)

people = cur.fetchall()

for person in people:
    print(person)
