from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId

notes_app = Flask(__name__.split('.')[0])
notes_app.secret_key = 'dev'
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, et cetera"

client = MongoClient('localhost', 27017, connect=False)

db = client.flask_db
notes = db.notes


@notes_app.route('/')
def home(error=None):
    if error:
        flash(error)
    if not 'email' in session:
        flash('please log in')
        return redirect(url_for('login'))
    all_notes = notes.find()
    return render_template('notes.html', notes=all_notes)
    

@notes_app.route('/add')    
def new_note():
    notes.insert_one({'title' : 'New Note', 'content' : lorem})
    return redirect(url_for('home'))


@notes_app.route('/<id_to_delete>/delete')
def delete_note(id_to_delete):
    if id_to_delete:
        deleted_note = notes.find_one({'_id': ObjectId(id_to_delete)})
        deleted_note_title = deleted_note['title']
        deleted_note = notes.delete_one({'_id': ObjectId(id_to_delete)})
        
        print(f"trying to delete")
        flash(f"deleted {deleted_note_title}")
    return redirect(url_for('home'))


@notes_app.route('/<note_id>/save')
def note_to_save(note_id):
    content = request.args.get('content')
    note_title = request.args.get('title')    
    notes.update_one({'_id' : ObjectId(note_id)}, 
                        { '$set' : {
                                'title' : note_title,
                                'content': content
                                }}, True)
    return redirect(url_for('home'))


@notes_app.route('/new')
def add_note():
    content = request.args.get('content')
    note_title = request.args.get('title')    
    notes.insert_one({'title' : note_title, 'content': content}, True)
    return redirect(url_for('home'))


@notes_app.route('/reset')
def reset_notes():
    notes.delete_many({})
    session.clear()
    flash('reset notes')
    return redirect(url_for('new_note'))


@notes_app.route('/debug')
def debug_info():
    flash(str(session))
    return redirect(url_for('home'))


@notes_app.route('/login')  
def login():
    return render_template("login.html")  
 
@notes_app.route('/success', methods=["POST"])  
def success():  
    if request.method == "POST":  
        session['email'] = request.form['email']
        print(session['email'])
        session.modified = True
        flash('You were successfully logged in')
    return redirect(url_for('home'))
    
 
@notes_app.route('/logout')  
def logout():  
    if 'email' in session:  
        session.pop('email')
        session.modified = True
        print(session)
        return redirect(url_for('home', message='successfully logged out'))
    else:  
        return '<p>user already logged out</p>'  
