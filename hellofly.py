import json
import os
import random
from typing import final

import requests
from dotenv import find_dotenv, load_dotenv
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())

app = Flask(__name__)

""" VVV Put DATABASE URI here! VVV """
app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)

class Person(db.Model):
    """Our database for logging in."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self) -> str:
        return f"Person with username: {self.username}"

with app.app_context():
    db.create_all()


@app.route('/')

def index():
    """The main code."""
    if __name__ =="__main__":
        app.run(debug=True)    
    people = Person.query.all()

    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

    """ VVV Put API Key Here VVV """
    key = ''

    headers = {
        'Authorization': 'Bearer %s' % key
    }

    parameters = {'location': 'San Marcos',
                 'term': 'Restaurant',
                 'radius': 5000,
                 'limit': 3,
                 'catagories': 'resturants, nightlife, arts'}

    response = requests.get(url = ENDPOINT, headers=headers, params=parameters)

    business_data = response.json()

    print(business_data)
    restaurant_name = ''
    restaurant_price = ''
    restaurant_address = ''

    for biz in business_data['businesses']:
        restaurant_name = (biz['name'])
        restaurant_price = (biz['price'])
        restaurant_address = (biz['location']['address1'])

    print(restaurant_name)
    print(restaurant_price)
    print(restaurant_address)

    return render_template('hello.html', restaurant_name=restaurant_name, restaurant_price=restaurant_price, restaurant_address=restaurant_address)