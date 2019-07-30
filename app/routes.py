from app import app
from app.models import model, formopener

import os
from flask import render_template, request, redirect
from flask_pymongo import PyMongo


# name of database
app.config['MONGO_DBNAME'] = 'FintechNotes' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://Ysbely05:3L4RUXYgdSg844u@cluster0-ykjcg.mongodb.net/FintechNotes?retryWrites=true&w=majority' 

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add', methods=[ 'GET','POST'])
def add():
    if request.method == "GET":
        return render_template('index.html')
    else:
        # return "Hello World"
        name = request.form['name']
        description = request.form['description']
        notesPictures = request.form['notesPictures']
        print(name)
        print(description)
        # print(notesPictures)
        
        FintechNotes = mongo.db.FintechNotes
        FintechNotes.insert({'name' : name, 'description' : description, 'notesPictures' : notesPictures})
        return render_template('results.html', notesPictures = notesPictures, name = name, description= description)

@app.route('/')
@app.route('/fintech')
def fintech():
    return render_template('fintech.html')

@app.route('/')
@app.route('/english')
def english ():
    return render_template('english.html')
    
@app.route('/')
@app.route('/math')
def math ():
    return render_template('math.html')

@app.route('/')
@app.route('/results')
def results ():
    return render_template('results.html')

    
    # ############################################################


