-- list all shows from hbtn_0d_tvshows_rate --
SELECT name, SUM(rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id

INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
