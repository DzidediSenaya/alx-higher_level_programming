-- Calculate the average temperature during July and August for each city and display the top 3 cities ordered by temperature (descending)
USE hbtn_0c_0;
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
