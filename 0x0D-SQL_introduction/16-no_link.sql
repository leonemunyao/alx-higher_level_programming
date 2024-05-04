-- A Script that lists all the records of the table second_table of the database hbtn_0c_0. No listing rows without the name value. Result should be listed in descending score.
SELECT * FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
