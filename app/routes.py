from app import app
from app.models import model, formopener
import os
#import magic
# import urllib.request
from flask import Flask, flash, request, redirect, render_template, session, url_for
from werkzeug.utils import secure_filename
from flask_pymongo import PyMongo
from gridfs import GridFS
#name of database
app.config['MONGO_DBNAME'] = 'FintechNotes' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://Ysbely05:3L4RUXYgdSg844u@cluster0-ykjcg.mongodb.net/FintechNotes?retryWrites=true&w=majority' 

mongo = PyMongo(app)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('notes.html')

@app.route('/add', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'GET':
        return render_template ('upload.html')
    else:
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/add')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)








@app.route('/')
@app.route('/notes')
def notes():
    return render_template('notes.html')

# @app.route('/add', methods=[ 'GET','POST'])
# def add():
#     if request.method == "GET":
#         return render_template('notes.html')
#     else:
#         # return "Hello World"
#         name = request.form['name']
#         description = request.form['description']
#         # notesPictures = request.form['notesPictures']
#         notesPictures = request.files.get('notesPictures')
#         print(type(notesPictures))
#         print(name)
#         print(description)
#         # print(notesPictures)
        
#         FintechNotes = mongo.db.FintechNotes
#         FintechNotes.insert({'name' : name, 'description' : description, 'notesPictures': notesPictures})
#         return render_template('results.html', name = name, description= description)


@app.route('/finTech')
def fintech():
    return render_template('finTech.html')

@app.route('/english')
def english ():
    return render_template('english.html')

@app.route('/math')
def math ():
    return render_template('math.html')


@app.route('/results')
def results ():
    return render_template('results.html')

@app.route('/upload')
def upload ():
    return render_template('upload.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if 'username' not in session:
        session['username'] = "newuser"
        session['username'] = "user"
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        if existing_user is None:
            users.insert({'name' : request.form['username'], 'password' : request.form['password']})
            session['username'] = request.form['username']
            return redirect(url_for('notes'))
        return 'That username already exists! Try logging in with the correct password.'
    nameDisplay = session['username']
    return render_template('signup.html', nameDisplay = nameDisplay)
    


    




