# TODO
# TODO
import cs50
import sys

if len(sys.argv) != 2:
    print("Usage: python roster.py house_name")
    exit(1)

db = cs50.SQL("sqlite:///students.db")

rows = db.execute('SELECT * FROM students WHERE house = ? ORDER BY last, first', sys.argv[-1])

for row in rows:
    print(row['first'] + ' ' + (row['middle'] + ' ' if row['middle'] else '') + row['last'] + ', born ' + str(row['birth']) )