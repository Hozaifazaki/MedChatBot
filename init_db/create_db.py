import sqlite3
from os.path import expanduser
db = sqlite3.connect('people.db')
columns = [
    "id INTEGER PRIMARY KEY",
    "lname VARCHAR UNIQUE",
    "fname VARCHAR",
    "timestamp DATETIME",
]
create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
cursor = db.cursor()
cursor.execute(create_table_cmd)