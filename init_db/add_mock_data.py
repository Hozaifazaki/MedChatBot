import sqlite3

conn = sqlite3.connect('people.db')
people = [
    "1, 'Fairy', 'Tooth', '2022-10-08 09:15:10'",
    "2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13'",
    "3, 'Bunny', 'Easter', '2022-10-08 09:15:27'",
]

# Add the mock data

for person in people:
    cmd = f"INSERT INTO person VALUES ({person})"
    conn.execute(cmd)

# Commit the inserting process
conn.commit()