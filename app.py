import json
import os
import random
from typing import final

import requests
from dotenv import find_dotenv, load_dotenv
from flask import Flask, render_template, request, url_for
import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:XgWmbZ0tdWKA0GS@project2-zachary-benavides-db.internal:5432'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Person with username: {self.username} and email: {self.email}"

@app.route("/")
def hello():
    people = Person.query.all()
    movie_id = random.randint(0,8)
    wiki_ext = ""

    if(movie_id == 0):
        movie_id = 1893
        wiki_ext = "Star_Wars:_Episode_I_–_The_Phantom_Menace"
    elif(movie_id == 1):
        movie_id = 1894
        wiki_ext = "Star_Wars:_Episode_II_–_Attack_of_the_Clones"
    elif(movie_id == 2):
        movie_id = 1895
        wiki_ext = "Star_Wars:_Episode_III_–_Revenge_of_the_Sith"
    elif(movie_id == 3):
        movie_id = 11
        wiki_ext = "Star_Wars_(film)"
    elif(movie_id == 4):
        movie_id = 1891
        wiki_ext = "The_Empire_Strikes_Back"
    elif(movie_id == 5):
        movie_id = 1892
        wiki_ext = "Return_of_the_Jedi"
    elif(movie_id == 6):
        movie_id = 140607
        wiki_ext = "Star_Wars:_The_Force_Awakens"
    elif(movie_id == 7):
        movie_id = 181808
        wiki_ext = "Star_Wars:_The_Last_Jedi"
    elif(movie_id == 8):
        movie_id = 181812
        wiki_ext = "Star_Wars:_The_Rise_of_Skywalker"

    movie_title = " "
    movie_tagline = " "
    movie_genres = " "
    movie_poster = "https://image.tmdb.org/t/p/w500"
    wiki_link = "https://en.wikipedia.org/wiki/"
    wiki_link += wiki_ext

    TMDB_MOVIE_SEARCH_API_REQUEST = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'

    response = requests.get(
        TMDB_MOVIE_SEARCH_API_REQUEST,
        params={
            'api_key': os.getenv('TMDB_API_KEY'),
            'language': "en",
        }
    )
    json_data = response.json()

    movie_title = json_data['title']
    movie_tagline = json_data['tagline']
    movie_genres = json_data['genres'][1]['name']
    movie_poster += json_data['poster_path']

    return render_template('hello.html', title=movie_title, tagline=movie_tagline, genres=movie_genres, poster=movie_poster, wikilink=wiki_link)