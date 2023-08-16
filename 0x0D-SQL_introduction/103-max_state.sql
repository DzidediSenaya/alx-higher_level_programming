-- Calculate the maximum temperature for each state and display the results ordered by state name
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
