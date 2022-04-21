# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, session
from flask_pymongo import PyMongo

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://innovators:tDxp5O4E312IPoiA@cluster0.nsm9q.mongodb.net/database?retryWrites=true&w=majority"


#Initialize PyMongo
mongo = PyMongo(app)

mongo.db.create_collection("post")

# -- Routes section --
# INDEX Route
# @app.route('/')
# @app.route('/')
# def index():
#     return render_template('feed.html')
# @app.route('/register')
# def register():
#     return render_template('signup.html')
# @app.route('/profile')
# def profile():
#     return render_template('profile.html')
# @app.route('/feed')
# def feed():
#     return render_template('feed.html')
# @app.route('/update')
# def update():
#     return render_template('update.html')