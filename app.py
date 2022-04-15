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
app.config['MONGO_URI'] = "<replace_with_real_mongodb_url>"

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