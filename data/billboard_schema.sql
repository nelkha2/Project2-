create table if not exists billboardhot100
(
	rankid integer not null
		constraint billboardhot100_pk
			primary key,
	rank integer,
	song_x varchar(128),
	artist_x varchar(128),
	year integer,
	song_y varchar(128),
	artist_y varchar(128),
	lyrics text,
	source integer,
	geniuslyrics text
);
