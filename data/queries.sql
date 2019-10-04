delete from billboardhot100
;
select rankid, rank, song_x, artist_x, year, song_y, artist_y, lyrics, geniuslyrics
from billboardhot100
order by rankid
;
select count(distinct(artist_y))
from billboardhot100
;
select Artist, count(*)
from billboardhot100songs
group by artist
order by count(*) desc
;
select artist_x, count(*)
from billboardhot100
group by artist_x
order by count(*) desc
;
select *
from billboardhot100
where geniuslyrics is NULL
order by rankid
;

--------Ideas---------
--1. Most words
--2. Least words
--3. Instrumentals? (not sure if can flag all these correctly)
--4. Top words from song titles?

--Things to fix--


