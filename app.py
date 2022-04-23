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

# mongo.db.create_collection("post")

# -- Routes section --
# INDEX Route
# @app.route('/')
# @app.route('/')
def index():
    return render_template('feed.html')
@app.route('/register')
def register():
    return render_template('signup.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/feed')
def feed():
    return render_template('feed.html')


@app.route('/')
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
    collection.insert_one({"postname":post_name, "posturl":post_url, "postmessage":post_message})
    # return render_template('create.html')
    return render_template("feed.html")

# @app.route('/update', methods=['GET','POST'])
# def update():
#     comments_collection = mongo.db.posts
#     if request.method =='GET':
#         posts = comments_collection.find({'hidden': 'false'})
#         return render_template('update.html', comments = posts)
#     # insert comment
#     text = request.form['text']
#     comments_collection.insert_one({'text':text, 'author': session['username'],'hidden':'false'})
#     return redirect('/update.html')
