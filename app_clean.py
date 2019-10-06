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

@app.route("/about")
def about():
    """Return the homepage."""
    return render_template("about.html")
    # return "Hello"

# Deploy data as json 
@app.route("/billboard/<rankid>")
def billboardYearEnd(rankid):
    sel =[
        HotOneHundred.rankid,
        HotOneHundred.rank,
        HotOneHundred.artist,
        HotOneHundred.song,
        HotOneHundred.geniuslyrics,
        HotOneHundred.artist_primary,
        HotOneHundred.decade,
        HotOneHundred.wordcount,
    ]
    results = db.session.query(*sel).filter(HotOneHundred.rankid == rankid).all()

    rankid_metadata ={}
    for result in results:
        rankid_metadata["rankid"] = result[0]
        rankid_metadata["rank"] = result[1]
        rankid_metadata["artist"] = result[2]
        rankid_metadata["song"] = result[3]
        rankid_metadata["geniuslyrics"] = result[4]
        rankid_metadata["artist_primary"] = result[5]
        rankid_metadata["decade"] = result[6]
        rankid_metadata["wordcount"] = result[7]
    print(rankid_metadata)
    return jsonify(rankid_metadata)

@app.route("/top-artists")
def topartists():
    """Return the homepage."""
    return render_template("top-artists.html")   

@app.route("/topartists-data")
def topartistsdata():
    top_results = engine.execute(f'select artist_primary, count(distinct song) from billboardhot100withlyrics group by artist_primary order by count(distinct song) desc LIMIT 25').fetchall()
    most_hits_json = [{i[0]: i[1]} for i in top_results]
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



