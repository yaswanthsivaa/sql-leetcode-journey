-- In MySQL, every subquery in FROM needs an alias.
SELECT Max(num) as num FROM ( SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(*) = 1 ) as t;
