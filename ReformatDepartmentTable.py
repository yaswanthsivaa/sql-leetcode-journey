# Reformat Department Table (LC 1179)
select id,
   Max(CASE WHEN month='Jan' THEN revenue END) as Jan_Revenue,
   Max(CASE WHEN month='Feb' THEN revenue END) as Feb_Revenue,
   Max(CASE WHEN month='Mar' THEN revenue END) as Mar_Revenue,
   Max(CASE WHEN month='Apr' THEN revenue END) as Apr_Revenue,
   Max(CASE WHEN month='May' THEN revenue END) as May_Revenue,
   Max(CASE WHEN month='Jun' THEN revenue END) as Jun_Revenue,
   Max(CASE WHEN month='Jul' THEN revenue END) as Jul_Revenue,
   Max(CASE WHEN month='Aug' THEN revenue END) as Aug_Revenue,
   Max(CASE WHEN month='Sep' THEN revenue END) as Sep_Revenue,
   Max(CASE WHEN month='Oct' THEN revenue END) as Oct_Revenue,
   Max(CASE WHEN month='Nov' THEN revenue END) as Nov_Revenue,
   Max(CASE WHEN month='Dec' THEN revenue END) as Dec_Revenue
FROM Department
GROUP BY id
