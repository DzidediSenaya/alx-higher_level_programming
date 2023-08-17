-- Import the database hbtn_0d_tvshows_rate dump to your MySQL
SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating_sum
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.id
ORDER BY rating_sum DESC;
