-- write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
-- Your query should output a table with a single column for the name of each person.
-- There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
-- Kevin Bacon himself should not be included in the resulting list.

-- 1. Kevin bacons id
-- 2. movie id  that has kevin id
-- 3. select people wtih those movie id
-- 4. Remove duplicates and kevin bacon


SELECT count(DISTINCT people.name)
FROM stars JOIN people ON stars.person_id = people.id
WHERE stars.movie_id IN
    (SELECT stars.movie_id
    FROM people JOIN stars ON stars.person_id = people.id
    WHERE name = "Kevin Bacon" and birth = 1958)
    
AND name != "Kevin Bacon";



