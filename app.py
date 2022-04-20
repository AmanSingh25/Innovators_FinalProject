# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_pymongo import PyMongo

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://test:A5ZOxxu5Bmp28n0u@cluster0.nsm9q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#Initialize PyMongo
mongo = PyMongo(app)

# -- Routes section --
# INDEX Route
@app.route('/')
@app.route('/login')
def index():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('signup.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/feed')
def feed():
    return render_template('feed.html')
@app.route('/update')
def update():
    return render_template('update.html')