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

create table if not exists billboardhot100songs
(
	rankid integer not null
		constraint billboard_hot_100_1965_to_2018_pk
			primary key,
	rank integer,
	song varchar(128),
	artist varchar(128),
	year integer
);

create unique index if not exists billboard_hot_100_1965_to_2018_rankid_uindex
	on billboardhot100songs (rankid);