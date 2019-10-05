delete from billboardhot100withlyrics
where rankid >= 304 and rankid < 501
;
select rankid, rank, song, artist, year, geniuslyrics
from billboardhot100withlyrics
order by rankid
;
select count(distinct(artist_y))
from billboardhot100withlyrics
;
select artist, count(distinct song)
from billboardhot100withlyrics
group by artist
order by count(distinct song) desc
;
select rankid, artist, song, wordcount, geniuslyrics
from billboardhot100withlyrics
order by wordcount desc
;
select rankid, rank, artist_primary, song, year
from billboardhot100withlyrics
where geniuslyrics is null
order by rankid
;
select count(*)
from billboardhot100withlyrics
where artist like '%featuring%';
;
update billboardhot100withlyrics
SET song = REPLACE(song,'"', '')
where rankid >= 301 and rankid < 400
;

--------Ideas---------
--1. Most words
--2. Least words
--3. Instrumentals? (not sure if can flag all these correctly)
--4. Top words from song titles?

--Things to fix--
--gangsta's paradise

select rankid, rank, artist, song, year, geniuslyrics
from billboardhot100withlyrics
--where lower(geniuslyrics) like '%instrumental%'
order by rankid
;
update billboardhot100withlyrics
set rankid = rankid - 9500
;
select *
from billboardhot100withlyrics
where geniuslyrics IS NULL or geniuslyrics = ''
;
update billboardhot100withlyrics
set geniuslyrics = '[Instrumental]'
where lower(geniuslyrics) = 'instrumental'
;
update billboardhot100withlyrics
set decade = '2010''s'
where year >= 2010
and year < 2020
;
select ltrim(left(artist, POSITION('featuring' IN artist)-1)) as "artist_primary", artist
from billboardhot100withlyrics
where artist like '%featuring%';
;
update billboardhot100withlyrics
set artist_primary = ltrim(left(artist, POSITION('featuring' IN artist)-1))
where artist like '%featuring%';
;
select artist_primary, sum(wordcount), round(avg(wordcount),0)
from billboardhot100withlyrics
group by artist_primary
order by sum(wordcount) desc
;
select artist_primary, song, year, geniuslyrics, wordcount
from billboardhot100withlyrics
where artist_primary = 'Madonna'
