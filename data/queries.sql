delete from billboardhot100
where rankid >= 304 and rankid < 501
;
select rankid, rank, song_x, artist_x, year, song_y, artist_y, lyrics, geniuslyrics
from billboardhot100
order by rankid
;
select count(distinct(artist_y))
from billboardhot100
;
select artist_x, count(distinct song_x)
from billboardhot100
group by artist_x
order by count(distinct song_x) desc
;
select artist, count(*)
from billboardhot100withlyrics
group by artist
order by count(*) desc
;
select *
from billboardhot100
where geniuslyrics is NULL
order by rankid
;
select count(*)
from billboardhot100
where artist_x like '%featuring%';
;
update billboardhot100
SET song_x = REPLACE(song_x,'"', '')
where rankid >= 301 and rankid < 400

--------Ideas---------
--1. Most words
--2. Least words
--3. Instrumentals? (not sure if can flag all these correctly)
--4. Top words from song titles?

--Things to fix--
--gangsta's paradise

select rankid, rank, artist_x, song_x, year, geniuslyrics
from billboardhot100
--where lower(geniuslyrics) like '%instrumental%'
order by rankid
;
update billboardhot100
set rankid = rankid - 9500
;
select *
from billboardhot100
where rankid = 362
;
update billboardhot100
set geniuslyrics = '[Instrumental]'
where lower(geniuslyrics) = 'instrumental'