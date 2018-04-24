from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask_oauthlib.client import OAuth
from flask import render_template
from flask_pymongo import PyMongo
from bson import ObjectId
from flask import flash
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from threading import Lock
 
import pprint
import os
import json
import pymongo
import sys

app = Flask(__name__)

app.debug = True #Change this to False for production
 
# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console

url = 'mongodb://{}:{}@{}:{}/{}'.format(
        os.environ["MONGO_USERNAME"],
        os.environ["MONGO_PASSWORD"],
        os.environ["MONGO_HOST"],
        os.environ["MONGO_PORT"],
        os.environ["MONGO_DBNAME"])
    
client = pymongo.MongoClient(url)
db = client[os.environ["MONGO_DBNAME"]]
collection = db['searchbar'] #put the name of your collection in the quotes

app.secret_key = os.environ['SECRET_KEY']
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key=os.environ['GOOGLE_CLIENT_ID'],
    consumer_secret=os.environ['GOOGLE_CLIENT_SECRET'],
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.context_processor
def inject_logged_in():
    return {"logged_in":('google_token' in session)}
 
@app.route('/')
def index():
    me="Not Logged In"
    if 'google_token' in session:
        me = google.get('userinfo')
        session['user_id'] = me.data['id']
        return render_template('home.html', listingTable=showListings(),display=displayListing())
    return render_template('home.html')
  
@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))
 
@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))
  
@app.route('/createListing',methods=['POST'])
def create_listing():
    collection.insert_one({"Listing":{"title":request.form['ltitle'],'description':request.form['des'],'paypaladdress':request.form['ppemail'],'user_id':session['user_id']}})
    return redirect(url_for('index'))
  
@app.route('/deleteListing',methods=['POST'])
def delete():
    #delete posts
    global collection
    collection.delete_one({"_id" : ObjectId(str(request.form['id']))})
    return showListings()
  
def showListings():
    tablestr='<table id="listingT"><tr><td>Title</td><td>Description</td><td>Paypal</td></tr>'
    table=""
    for doc in collection.find():
        if session['user_id'] == doc['Listing']['user_id']:
            tablestr += '<tr class="listing"><td>'
            tablestr += str(doc['Listing']['title'])
            tablestr += "</td><td>"
            tablestr += str(doc['Listing']['description'])
            tablestr += "</td><td>"
            tablestr += str(doc['Listing']['paypaladdress'])
            tablestr += "</td><td>"
            tablestr += '<button class="btn btn-danger deleteBtn" onclick="deletefunction()" value="' + str(doc.get('_id')) + '">Delete</button></td></tr>'
    tablestr += "</table>"
    table += Markup(tablestr)
    return table
   
def displayListing():
	listing=''
	for doc in collection.find():
		listing+='<figure class="figure">'
		listing+='<img src="https://lh3.googleusercontent.com/9hfLHZyz6OM0k5iJcs1HSJ-jAG0lllNiuvI0_TFmSc2Zm9nmUC548Ppyi69xSZWznZQb=s128" class="figure-img img-fluid rounded" alt="somerounded square">'
		listing+='<figcaption class="figure-caption text-center">' + str(doc['Listing']['title']) + '</figcaption>'
		listing+='<figcaption class="figure-caption text-center">' + str(doc['Listing']['description']) + '</figcaption>'
		listing+='</figure>'
	return Markup(listing)
   
@app.route('/search', methods=['POST']) 
def search_bar():
    try:
        search = {}
        search['key'] = request.form['searchvalue']
        print(collection.find(search))
    except Exception as e:
        print(e)
    return redirect(url_for('index'))
 
@app.route('/login/authorized')
@google.authorized_handler
def authorized(resp):
    if resp is None:
        me = 'Access denied: reason=%s error=%s' + request.args['error_reason'] + request.args['error_description']
    session['google_token'] = (resp['access_token'], '')
    return redirect(url_for('index'))
   
@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')
 
if __name__ == '__main__':
    app.run()
