SELECT 
user_id, (CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2)))) as name 
FROM USERS
ORDER BY user_id;
