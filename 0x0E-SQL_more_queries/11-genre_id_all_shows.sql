-- Switch to the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select all shows with their linked genres and display NULL for shows without a genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
