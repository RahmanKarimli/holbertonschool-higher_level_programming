-- My genres
SELECT tg.name
FROM tv_show_genres AS tsg
INNER JOIN tv_shows AS ts ON ts.id=tsg.show_id
INNER JOIN tv_genres AS tg ON tg.id=tsg.genre_id
WHERE ts.title='Dexter'
ORDER BY tg.name ASC;
