--Import the database dump from hbtn_0d_tvshows_rate to your MySQL server
SELECT tv_genres.name, SUM(tv_show_genres.rating) AS rating_sum
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
