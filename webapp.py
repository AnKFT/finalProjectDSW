from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask_oauthlib.client import OAuth
from flask import render_template
from flask_pymongo import PyMongo
from bson import ObjectId
from flask import flash
 
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
    request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    consumer_key=os.environ['GOOGLE_CLIENT_ID'],
    consumer_secret=os.environ['GOOGLE_CLIENT_SECRET'])

@app.route('/')
def index():
    me="text"
    if 'google_token' in session:
        me = google.get('userinfo')
    return render_template('home.html', info=me)
  
@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))
 
@app.route('/login/authorized')
@google.authorized_handler
def authorized(resp):
    if resp is None:
        me = 'Access denied: reason=%s error=%s' + request.args['error_reason'] + request.args['error_description']
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    return render_template('home.html', info=me)
   
@google.tokengetter
def get_access_token():
    return session.get('access_token')

if __name__ == '__main__':
    app.run()
