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
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Keefac85?@localhost/Project_2'
db = SQLAlchemy(app)

#Reflect existing db into model 
Base = automap_base()

#Reflect tables 
Base.prepare(db.engine, reflect=True)

#Save references to each table 
HotOneHundred = Base.classes.billboardhotsongs

@app.route("/")
def index():
    """Return the homepage."""
    # return render_template("index.html")
    return "Hello"

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
   

if __name__ == "__main__":
    app.run()



