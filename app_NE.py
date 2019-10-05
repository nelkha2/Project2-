import os
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

#Flask App
app = Flask(__name__)

# Connecting to Postgres (//<username:password>@localhost/<local DB name>)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Keefac85?@localhost/Project_2'
db = SQLAlchemy(app)


#Connecting to existing table: billboardhot100songs
class Billboardhot100songs(db.Model):
    __tablename__ = 'billboardhot100songs'
    rankid = db.Column('rankid', db.Integer, primary_key=True)
    rank = db.Column('rank', db.Integer)
    song = db.Column('song', db.Unicode)
    artist = db.Column('artist', db.Unicode)
    year = db.Column('year', db.Integer)

# Connecting to existing table: billboardhot100_lyrics (*change based on local name)
class Billboardhot100_lyrics(db.Model):
    __tablename__ = 'billboardhot100_lyrics'
    rankid = db.Column('rankid', db.Integer, primary_key=True)
    rank = db.Column('rank', db.Integer)
    song_x = db.Column('song_x', db.Unicode)
    artist_x = db.Column('artist_x', db.Unicode)
    year = db.Column('year', db.Integer)
    song_y = db.Column('song_y', db.Unicode)
    artist_y = db.Column('artist_y', db.Unicode)
    lyrics = db.Column('lyrics', db.Unicode)
    source = db.Column('source', db.Float)
    lyricstatus = db.Column('lyricstatus', db.Integer)
    geniuslyrics = db.Column('geniuslyrics', db.Unicode)



@app.route("/")
def index():
    """Return the homepage."""
    # return render_template("index.html")
    return "Hello"
    

if __name__ == "__main__":
    app.run()

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


