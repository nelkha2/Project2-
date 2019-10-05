create table if not exists billboardhot100withlyrics
(
	rankid integer not null
		constraint billboardhot100withlyrics_pk
			primary key,
	rank integer,
	artist varchar(128),
    song varchar(128),
	year integer,
    geniuslyrics text,
    artist_primary varchar(128),
    decade varchar(20),
    wordcount int
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