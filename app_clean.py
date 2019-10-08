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
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data/data.sqlite'
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{u}:{p}@ec2-107-21-120-104.compute-1.amazonaws.com:5432/d6svjqnlm9q76b'
db = SQLAlchemy(app)

#Reflect existing db into model 
Base = automap_base()

#Reflect tables 
Base.prepare(db.engine, reflect=True)

#Save references to each table 
HotOneHundred = Base.classes.billboardhot100withlyrics

#Engine
engine = create_engine(f'postgresql://{u}:{p}@ec2-107-21-120-104.compute-1.amazonaws.com:5432/d6svjqnlm9q76b')

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")
    # return "Hello"

@app.route("/fun-facts")
def about():
    """Return the homepage."""
    return render_template("fun-facts.html")
    # return "Hello"

@app.route("/search")
def search():
    """Return the search page."""
    return render_template("search.html")
    # return "Hello"    

# Deploy data as json 
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
    most_hits_json = [{i[0]: i[1]} for i in top_results]
    return jsonify(most_hits_json)

@app.route("/yearlyhits-data/<timeframe>")
def yearlyhitsdata(timeframe):
    print(timeframe)
    top_results = engine.execute(f"select artist_primary, count(distinct song) from billboardhot100withlyrics where year = {timeframe} group by artist_primary having count(distinct song) > 1 order by count(distinct song) desc LIMIT 10").fetchall()
    most_hits_json = [{i[0]: i[1]} for i in top_results]
    return jsonify(most_hits_json)

@app.route("/lyrics")
def lyrics():
    """Return the lyrics page."""
    return render_template("lyrics.html")

@app.route("/lyrics-data/<timeframe>")
def mostverbosedata(timeframe):
    print(timeframe)
    if timeframe == 'All-Time':
        top_results = engine.execute(f'select artist_primary, round(avg(wordcount),0) from billboardhot100withlyrics group by artist_primary having count(artist_primary) > 1 order by avg(wordcount) desc LIMIT 25').fetchall()
    else:
        top_results = engine.execute(f"select artist_primary, round(avg(wordcount),0) from billboardhot100withlyrics where decade = '{timeframe}' group by artist_primary having count(artist_primary) > 1 order by avg(wordcount) desc LIMIT 25").fetchall()
    most_hits_json = [{i[0]: int(i[1])} for i in top_results]
    return jsonify(most_hits_json)

@app.route("/obscene-data/<timeframe>")
def topoffensivedata(timeframe):
    print(timeframe)
    if timeframe == 'All-Time':
        top_results = engine.execute(f'select artist_primary, round(avg(explicit_word_count),0) from billboardhot100withlyrics where explicit_word_count is not null group by artist_primary having count(artist_primary) > 1 order by avg(explicit_word_count) desc LIMIT 25').fetchall()
    else:
        top_results = engine.execute(f"select artist_primary, round(avg(explicit_word_count),0) from billboardhot100withlyrics where decade = '{timeframe}' and explicit_word_count is not null group by artist_primary having count(artist_primary) > 1 order by avg(explicit_word_count) desc LIMIT 25").fetchall()
    most_hits_json = [{i[0]: int(i[1])} for i in top_results]
    return jsonify(most_hits_json)   

@app.route("/obsceneyearly-data")
def obsceneyearly():
    # print(timeframe)
    top_results = engine.execute(f'select year, sum(explicit_word_count), round(avg(explicit_word_count),0) from billboardhot100withlyrics where explicit_word_count is not null group by year order by year').fetchall()
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



