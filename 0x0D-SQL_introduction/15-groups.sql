-- A Script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0. The column should display score and number of records. The list should be sorted by the number of records in descending order.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
