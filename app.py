# -- Import section --
import os
from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for, session
from flask_pymongo import PyMongo
import secrets
#from organizations_info import organizations_info
import bcrypt

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://innovators:tDxp5O4E312IPoiA@cluster0.nsm9q.mongodb.net/database?retryWrites=true&w=majority"

secret_key = os.environ.get('MONGO_URI')
# app.config['MONGO_URI'] = secret_key
app.secret_key = secrets.token_urlsafe(16)

#Initialize PyMongo
mongo = PyMongo(app)

#mongo.db.create_collection("post")
#mongo.db.create_collection("users_info")
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])

def login():

    if request.method == "POST":
        users = mongo.db.users_info
        #search for username in database
        login_user = users.find_one({'name': request.form['username']})

        #if username in database
        if login_user:
            db_password = login_user['password']
            #encode password
            password = request.form['password'].encode("utf-8")
            #compare username in database to username submitted in form
            if bcrypt.checkpw(password, db_password):
                #store username in session
                session['username'] = request.form['username']
                return render_template('index.html')
            else:
                return 'Invalid username/password combination.'
        else:
            return 'User not found. Please try Signing in'
    else:
        return render_template('login.html')

#SignUp Route

@app.route('/signup', methods=['GET', 'POST'])
def singup():
    if request.method == "POST":
        users = mongo.db.users_info
        #search for username in database
        existing_user = users.find_one({'name': request.form['username']})

        #if user not in database
        if not existing_user:
            username = request.form['username']
            #
            if request.form['password'] == '':
                return
            #encode password for hashing
            password = (request.form['password']).encode("utf-8")
            password1 = (request.form['password1']).encode("utf-8")
            #check passwords equal
            
            #hash password
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password, salt)
            hashed1 = bcrypt.hashpw(password1, salt)
            image_url = request.form['image_url']
            
            #add new user to database
            users.insert_one({'name': username, 'password': hashed, 'image_url' : image_url})
            #store username in session
            session['username'] = request.form['username']
            return render_template('login.html')
        else:
            return 'Username already registered.Try logging in.'  
    else:
        return render_template('signup.html')
