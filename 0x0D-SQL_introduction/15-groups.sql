-- displays the number of recods with equal score on your database --
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score
