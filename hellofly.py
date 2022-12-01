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
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:IjV6w6UN41ga4Tq@long-silence-6282-db.internal:5432'

db = SQLAlchemy(app)

class Person(db.Model):
    """Our database for logging in."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

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
    key = 'VJFY8V0sueomVwnKd8j9CvryLMtuJBfMitN2_GPNAKa8YjIXCyzGsOngs1pargTGNk2Jb4jy50PZi24Yzb1lyr12m773jXkyE71A9oLs28l6Qkg-yOFzJnfq8XqGY3Yx'

    headers = {
        'Authorization': 'Bearer %s' % key
    }

    parameters = {'location': 'San Marcos',
                'term': 'Restaurant',
                'radius': 5000,
                 'limit': 50}

    response = requests.get(url = ENDPOINT, headers=headers, params=parameters)

    business_data = response.json()

    print(business_data)

    restaurant_name = ''
    restaurant_price = ''
    restaurant_address = ''
    restaurant_image_url = ''
    restaurant_is_closed = True
    x = random.randint(0,49)
    count = 0

    for biz in business_data['businesses']:
        if count == x:
            restaurant_name = (biz['name'])
            restaurant_price = (biz['price'])
            restaurant_address = (biz['location']['address1'])
            restaurant_image_url = (biz['image_url'])
            restaurant_is_closed = (biz['is_closed'])
        count = count + 1

    if(restaurant_is_closed == True):
        restaurant_is_closed = 'Closed'
    else:
        restaurant_is_closed = 'Open'
    
    return render_template('hello.html', restaurant_name=restaurant_name, restaurant_price=restaurant_price,
     restaurant_address=restaurant_address, restaurant_image_url=restaurant_image_url, restaurant_is_closed=restaurant_is_closed)