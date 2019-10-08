import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import u,p

#Flask App
app = Flask(__name__)

# Connecting to Postgres (//<username:password>@localhost/<local DB name>)
<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Keefac85?@localhost/Project_2'
# app.config["SQLALCHEMY_DATABASE_URI"] = f'postgres://{u}:{p}@ec2-107-21-120-104.compute-1.amazonaws.com:5432/d6svjqnlm9q76b'
=======
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data/data.sqlite'
<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Keefac85?@localhost/Project_2'
>>>>>>> Nader_new
=======
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{u}:{p}@ec2-107-21-120-104.compute-1.amazonaws.com:5432/d6svjqnlm9q76b'
>>>>>>> 0b7845f211e5d9badcf5c30cc40d2f7fd7cc6ce5
db = SQLAlchemy(app)

#Reflect existing db into model 
Base = automap_base()

#Reflect tables 
Base.prepare(db.engine, reflect=True)

#Save references to each table 
<<<<<<< HEAD
<<<<<<< HEAD
HotOneHundred = Base.classes.billboardhot100songs


#Connecting to existing table: billboardhot100songs
# class Billboardhot100songs(db.Model):
#     __tablename__ = 'billboardhot100songs'
#     rankid = db.Column('rankid', db.Integer, primary_key=True)
#     rank = db.Column('rank', db.Integer)
#     song = db.Column('song', db.Unicode)
#     artist = db.Column('artist', db.Unicode)
#     year = db.Column('year', db.Integer)

# # Connecting to existing table: billboardhot100_lyrics (*change based on local name)
# class Billboardhot100_lyrics(db.Model):
#     __tablename__ = 'billboardhot100_lyrics'
#     rankid = db.Column('rankid', db.Integer, primary_key=True)
#     rank = db.Column('rank', db.Integer)
#     song_x = db.Column('song_x', db.Unicode)
#     artist_x = db.Column('artist_x', db.Unicode)
#     year = db.Column('year', db.Integer)
#     song_y = db.Column('song_y', db.Unicode)
#     artist_y = db.Column('artist_y', db.Unicode)
#     lyrics = db.Column('lyrics', db.Unicode)
#     source = db.Column('source', db.Float)
#     lyricstatus = db.Column('lyricstatus', db.Integer)
#     geniuslyrics = db.Column('geniuslyrics', db.Unicode)

    
=======
HotOneHundred = Base.classes.billboardhotsongs

#Engine
engine = create_engine('postgresql://postgres:Keefac85?@localhost/Project_2')
>>>>>>> Nader_new
=======
HotOneHundred = Base.classes.billboardhot100withlyrics

#Engine
engine = create_engine(f'postgresql://{u}:{p}@ec2-107-21-120-104.compute-1.amazonaws.com:5432/d6svjqnlm9q76b')
>>>>>>> 0b7845f211e5d9badcf5c30cc40d2f7fd7cc6ce5

@app.route("/")
def index():
    """Return the homepage."""
<<<<<<< HEAD
    # return render_template("index.html")
    return "Hello"
=======
    return render_template("index.html")
    # return "Hello"
>>>>>>> Nader_new

@app.route("/about")
def about():
    """Return the homepage."""
    return render_template("about.html")
    # return "Hello"

@app.route("/search")
def search():
    """Return the search page."""
    return render_template("search.html")
    # return "Hello"    

# Deploy data as json 
<<<<<<< HEAD
@app.route("/billboard/<rankid>")
def billboardYearEnd(rankid):
    sel =[
        HotOneHundred.rankid,
        HotOneHundred.rank,
<<<<<<< HEAD
        HotOneHundred.song,
        HotOneHundred.artist,
        HotOneHundred.year,
=======
        HotOneHundred.artist,
        HotOneHundred.song,
        HotOneHundred.geniuslyrics,
        HotOneHundred.artist_primary,
        HotOneHundred.decade,
        HotOneHundred.wordcount,
>>>>>>> Nader_new
    ]
    results = db.session.query(*sel).filter(HotOneHundred.rankid == rankid).all()

    rankid_metadata ={}
    for result in results:
        rankid_metadata["rankid"] = result[0]
        rankid_metadata["rank"] = result[1]
<<<<<<< HEAD
        rankid_metadata["song"] = result[2]
        rankid_metadata["artist"] = result[3]
        rankid_metadata["year"] = result[4]
    print(rankid_metadata)
    return jsonify(rankid_metadata)
    # test = {"Sample1": 5, "Sample2": 10}
    # set = Billboardhot100songs.query.all()
    # return jsonify(set)

if __name__ == "__main__":
    app.run()
    # app.run(debug=True)

# -------------------------------------------#
# Research - Notes 

# --Creating Table in DB via flask--
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username

# --Importing data from postgres--
# Resource: connecting to existing DB and running queries in Anaconda 
# https://www.youtube.com/watch?v=Tu4vRU4lt6k
# Anaconda coding - 
# cd "folder path"
# from "python folder name w/o extension" import "class name"
# to verify connection - 
# XX = "Class name".query.all()
# printing specific column- 
# for z in XX:
#  print(z."column name")
=======
        rankid_metadata["artist"] = result[2]
        rankid_metadata["song"] = result[3]
        rankid_metadata["geniuslyrics"] = result[4]
        rankid_metadata["artist_primary"] = result[5]
        rankid_metadata["decade"] = result[6]
        rankid_metadata["wordcount"] = result[7]
    print(rankid_metadata)
    return jsonify(rankid_metadata)

@app.route("/Mosthits")
def billboard():
    top_results = engine.execute(f'select artist_primary, count(distinct song) from billboardhotsongs group by artist_primary order by count(distinct song) desc LIMIT 25').fetchall()
=======
@app.route("/search/<artist>")
def billboardYearEnd(artist):
    # sel =[
    #     HotOneHundred.rankid,
    #     HotOneHundred.rank,
    #     HotOneHundred.artist,
    #     HotOneHundred.song,
    #     HotOneHundred.artist_primary,
    #     HotOneHundred.decade,
    #     HotOneHundred.wordcount,
    #     HotOneHundred.geniuslyrics,
    # ]
    
    #results = db.session.query(*sel).filter(HotOneHundred.artist == artist).all()
    artist_results = engine.execute(f"select rankid, rank, artist, song, artist_primary, decade, wordcount, geniuslyrics, year from billboardhot100withlyrics where artist_primary = '{artist}' order by rankid").fetchall()

    print(artist_results)

    artist_metadata = []
    for result in sorted(artist_results):
        new_result = { 'rankid': result[0], 'rank': result[1], 'artist': result[2], 'song': result[3], 'artist_primary': result[4], 'decade': result[5], 'wordcount': result[6], 'geniuslyrics': result[7] , 'year': result[8]}
        artist_metadata.append(new_result)
        # artist_metadata.append({'rankid' : result[0]})
        # artist_metadata.append({"rank" : result[1]} )
        # artist_metadata.append({"artist" : result[2]} )
        # artist_metadata.append({"song" : result[3]} )
        # artist_metadata.append({"geniuslyrics" : result[4]} )
        # artist_metadata.append({"artist_primary" : result[5]} )
        # artist_metadata.append({"decade" : result[6]} )
        # artist_metadata.append({"wordcount" : result[7]} )
    
    #print(artist_metadata)
    
    return jsonify(artist_metadata)

@app.route("/top-artists")
def topartists():
    """Return the homeptop artists page."""
    return render_template("top-artists.html")    

@app.route("/topartists-data/<timeframe>")
def topartistsdata(timeframe):
    print(timeframe)
    if timeframe == 'All-Time':
        top_results = engine.execute(f'select artist_primary, count(distinct song) from billboardhot100withlyrics group by artist_primary order by count(distinct song) desc LIMIT 25').fetchall()
    else:
        top_results = engine.execute(f"select artist_primary, count(distinct song) from billboardhot100withlyrics where decade = '{timeframe}' group by artist_primary order by count(distinct song) desc LIMIT 25").fetchall()
>>>>>>> 0b7845f211e5d9badcf5c30cc40d2f7fd7cc6ce5
    most_hits_json = [{i[0]: i[1]} for i in top_results]
    return jsonify(most_hits_json)

@app.route("/lyrics")
def lyrics():
    """Return the lyrics page."""
    return render_template("lyrics.html")

@app.route("/lyrics-data/<timeframe>")
def topoffensivedata(timeframe):
    print(timeframe)
    if timeframe == 'All-Time':
        top_results = engine.execute(f'select artist_primary, round(avg(wordcount),0) from billboardhot100withlyrics group by artist_primary order by avg(wordcount) desc LIMIT 25').fetchall()
    else:
        top_results = engine.execute(f"select artist_primary, round(avg(wordcount),0) from billboardhot100withlyrics where decade = '{timeframe}' group by artist_primary order by avg(wordcount) desc LIMIT 25").fetchall()
    most_hits_json = [{i[0]: int(i[1])} for i in top_results]
    return jsonify(most_hits_json)


@app.route("/decades")
def decades():
    # List of decades 
    # music_decades = engine.execute(f'select decades, from billboardhotsongs').fetchall()
    # data_decades = [{i[0]: length.music_decades} for i in music_decades]
    # return jsonify(data_decades)

    # Sql query via Pandas
    stmt = db.session.query(HotOneHundred).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    return jsonify(list(df.columns)[6:])   

if __name__ == "__main__":
    app.run()

>>>>>>> Nader_new


