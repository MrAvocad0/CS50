# TODO
import cs50
import csv
import sys

if len(sys.argv) != 2:
    print("Usage: python import.py file.csv")
    exit(1)

db = cs50.SQL("sqlite:///students.db")

with open(sys.argv[1], "r") as characters:

    # Create DictReader
    reader = csv.DictReader(characters)

    # Iterate over TSV file
    for row in reader:
        # split function to split names by blank spaces
        name = row['name'].split()
        first, middle ,last = name[0], name[1] if len(name) == 3 else None, name[-1]
        # if len(name) == 3:
        #     first, middle, last = name
        # else:
        #     first, last = name
        #     middle = None


        house = row['house']
        birth = row['birth']

    # Insert into db
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, house, birth)



