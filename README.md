# Python-SQL-
CS50 coursework Python and SQL.

Houses Folder:
characters.csv is a file with a list of names, DOB and houses they are in.
import.py - takes the csv file and puts it into a database with other list of names, DOB and houses they are in.
            We can later use SQL commmands to pull our data from.
roster.py - Short code to pull character data by house, data is ordered by last name then first name.
students.db - the database of students data along with the imported data from character.csv

Movies Folder:
Several SQL command lines to pull information from Movies.db.

Movies.db - Database with several tables.

Each table has a their own set of columns, given below.
Tables:
Movies - Movie information - id, title and year it was released
-id
-title
-year
People - Peoples information, their Id along with their name and birthdate.
-id
-name
-birth
Directors - directors id and what movie they starred in connected by movie id.
-movie_id
-person_id
Stars - Actors id and what movie they starred in connected by movie id.
-movie_id
-person_id
Ratings - movies, their rating and number of votes made.
-Movie_id
-raiting
-votes
