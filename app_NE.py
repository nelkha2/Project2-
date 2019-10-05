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
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Keefac85?@localhost/Project_2'
# app.config["SQLALCHEMY_DATABASE_URI"] = f'postgres://{u}:{p}@ec2-107-21-120-104.compute-1.amazonaws.com:5432/d6svjqnlm9q76b'
db = SQLAlchemy(app)

#Reflect existing db into model 
Base = automap_base()

#Reflect tables 
Base.prepare(db.engine, reflect=True)

#Save references to each table 
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
        HotOneHundred.song,
        HotOneHundred.artist,
        HotOneHundred.year,
    ]
    results = db.session.query(*sel).filter(HotOneHundred.rankid == rankid).all()

    rankid_metadata ={}
    for result in results:
        rankid_metadata["rankid"] = result[0]
        rankid_metadata["rank"] = result[1]
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


