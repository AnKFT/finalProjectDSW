from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask_oauthlib.client import OAuth
from flask import render_template
from flask_pymongo import PyMongo
from bson import ObjectId
from flask import flash
from flask import Flask, redirect, url_for, session
from flask_oauth import OAuth
 
import pprint
import os
import json
import pymongo
import sys

app = Flask(__name__)

app.debug = True #Change this to False for production
 
# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console

app.secret_key = os.environ['SECRET_KEY']
oauth = OAuth(app)

google = oauth.remote_app('google',
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email', 'response_type': 'code'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_key=os.environ['GOOGLE_CLIENT_ID'],
    consumer_secret=os.environ['GOOGLE_CLIENT_SECRET'])

@app.route('/')
def index():
    return render_template('home.html')
  
@app.route('/login')
def login():
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)
 
@app.route('/login/authorized')
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return render_template('home.html')
 
@google.tokengetter
def get_access_token():
    return session.get('access_token')

if __name__ == '__main__':
    app.run()
