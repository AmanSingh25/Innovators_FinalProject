# -- Import section --
import os
from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for, session
from flask_pymongo import PyMongo
from model import *
import secrets
import bcrypt

# -- Initialization section --
app = Flask(__name__)

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://innovators:tDxp5O4E312IPoiA@cluster0.nsm9q.mongodb.net/database?retryWrites=true&w=majority"


# -- Session data --
app.secret_key = secrets.token_urlsafe(16)


#Initialize PyMongo
mongo = PyMongo(app)

# mongo.db.create_collection("post")

# -- Routes section --
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
            image_url = login_user['image_url']
            #encode password
            password = request.form['password'].encode("utf-8")
            #compare username in database to username submitted in form
            if bcrypt.checkpw(password, db_password):
                #store username and user's image in session
                session['username'] = request.form['username']
                session['image_url'] = image_url
                return render_template('feed.html')
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
        user_name = request.form['username']
        password_unencrypted = request.form['password']

        #checks if both password and username format is empty
        if is_all_empty(user_name) and is_all_empty(password_unencrypted):
            return render_template("signup.html")
        #checks if username format is empty
        elif is_all_empty(user_name):
            return render_template("signup.html")
        #checks if the password is empty
        elif is_all_empty(password_unencrypted):
            return render_template("signup.html")
        #checks if the password is valid or not
        elif not is_valid_password(password_unencrypted):
            return render_template("signup.html")
        
        existing_user = users.find_one({'name':user_name})

        #if user not in database
        if not existing_user:
            username = request.form['username']
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


@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        #render the form to populate the required parameters
        return render_template("create.html")
    else:
        #assign from data to varaibles
        post_name = request.form['postname']
        post_url = request.form['posturl']
        post_message = request.form['postmessage']    
    collection = mongo.db.post

     #insert an entry to the database using the variables declared above
    collection.insert_one({"postname":post_name, "posturl":post_url, "postmessage":post_message, "user":session['username'], "profile_url":session['image_url']})
    return render_template("create.html")


#allfeed route

@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == "GET":
        #render the form to populate the required parameters
        return render_template("delete.html")
    else:
        #assign from data to varaibles
        post_name = request.form['postname']
        post_url = request.form['posturl']
        post_message = request.form['postmessage']    
    collection = mongo.db.post

     #delete an entry to the database using the variables declared above
    collection.delete_one({"postname":post_name, "posturl":post_url, "postmessage":post_message})
    # return render_template('create.html')
    return render_template("feed.html")

@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == "GET":
        #render the form to populate the required parameters
        return render_template("update.html")
    else:
        #assign from data to varaibles
        old_post_name = request.form['postname']
        old_post_url = request.form['posturl']
        old_post_message = request.form['postmessage']    
    collection = mongo.db.post
    new_post_name = { "$set": { "postname":old_post_name } }
    new_post_url = { "$set": {"posturl":old_post_url }}
    new_post_message = { "$set": { "postmessage":old_post_message} }
     #delete an entry to the database using the variables declared above
    collection.update_one({"postname":old_post_name, "posturl":old_post_url, "postmessage":old_post_message},{"postname":new_post_name, "posturl":new_post_url, "postmessage":new_post_message})
    # return render_template('create.html')
    return render_template("feed.html")

#allfeed rouute
@app.route('/feed')
def feed():
    collection = mongo.db.post
    feeds = collection.find_one({'postname': 'First Post by Team Innovators'})
    # sort the database alphabetically based on their name and render all the user name to the page in sorted manner
    return render_template('feed.html', feeds = feeds)


