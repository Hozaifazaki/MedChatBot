import sqlite3
from os.path import expanduser
db_dir = expanduser("~")
db = sqlite3.connect(db_dir+'/people.db')
columns = [
    "id INTEGER PRIMARY KEY",
    "lname VARCHAR UNIQUE",
    "fname VARCHAR",
    "timestamp DATETIME",
]
create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
cursor = db.cursor()
cursor.execute(create_table_cmd)