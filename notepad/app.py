import pickle
from flask import make_response, render_template, request, redirect, url_for
from flask import Flask
from jinja2 import filters
import notes.notes as notes
import pickle

notes_app = Flask(__name__.split('.')[0])
note_list = {}
message = None

@notes_app.route('/')
def display_notes():
    global message
    print(note_list)
    return render_template('home.html', notes_to_display=list(note_list.values()), message=message)

@notes_app.route('/save')
def save_notes():
    global message
    with open('notes/saved_notes.bin', "wb") as file:
        pickle.dump(note_list, file)
    message = f"notes saved"
    return redirect(url_for('display_notes'))
                    
@notes_app.route('/load') 
def load_notes():
    global message
    global note_list
    with open('notes/saved_notes.bin', "rb") as file:
        note_list = pickle.load(file)
    message = f"notes loaded"
    return redirect(url_for('display_notes'))
    
@notes_app.route('/create')
def add_note():
    new_note = notes.add_note(note_list, request.args.get('title'), request.args.get('content'))
    return redirect(url_for('display_notes'))

@notes_app.route('/input')
@notes_app.route('/input/<note>')
def input_note(note=None):
    if note:
        input_note = note_list[note]
        return render_template('input.html', note=input_note)
    else:
        return render_template('input.html')
    
@notes_app.route('/delete/<note>')
def delete_note(note):
    global message
    message = f"note '{note_list[note].title}' deleted"
    note_list.pop(note)
    return redirect(url_for('display_notes'))
        