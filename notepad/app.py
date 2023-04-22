from flask import render_template, request, redirect, url_for
from flask import Flask
from jinja2 import filters
import notes.notes as notes

notes_app = Flask(__name__.split('.')[0])
note_list = {}

@notes_app.route('/')
def display_notes():
    print(note_list)
    return render_template('home.html', notes_to_display=list(note_list.values()))

    
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