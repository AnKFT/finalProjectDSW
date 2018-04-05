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

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
