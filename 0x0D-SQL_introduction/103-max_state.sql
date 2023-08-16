-- Calculate the maximum temperature for each state and display the results ordered by state name
USE hbtn_0c_0;
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
