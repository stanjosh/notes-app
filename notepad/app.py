import pickle
from flask import Flask, render_template, request, redirect, url_for
import notes.notes as notes


notes_app = Flask(__name__.split('.')[0])
note_list = {}
message = None

@notes_app.route('/')
def display_notes():
    global message
    status = message
    message = None
    print(note_list)
    load_notes()
    return render_template('notes.html', notes_to_display=list(note_list.values()), message=status)
    
@notes_app.route('/reset')
def reset_notes():
    note_list.clear()
    add_note(note_list)
    with open('notes/saved_notes.bin', "wb+") as file:
        pickle.dump(note_list, file)
    return redirect(url_for('display_notes'))

@notes_app.route('/save')
@notes_app.route('/save/<note>')
def save_notes(note=None):
    global message
    if note:
        notes.edit(note_list, request.args.get('title'), request.args.get('content'))
    with open('notes/saved_notes.bin', "wb+") as file:
        pickle.dump(note_list, file)
    message = f"notes saved"
    return redirect(url_for('display_notes'))
                    
@notes_app.route('/load') 
def load_notes():
    global message
    global note_list
    with open('notes/saved_notes.bin', "rb+") as file:
        note_list = pickle.load(file)
    message = f"notes loaded"
    return redirect(url_for('display_notes'))
    

@notes_app.route('/edit')
@notes_app.route('/edit/<note>')
def edit_note(note=None):
    return render_template('edit.html', note=note_list[note])

@notes_app.route('/add')
@notes_app.route('/add/<note>')
def add_note(note=None):
    note = note_list[notes.add(note_list)] if not note else note
    return render_template('edit.html', note=note)

@notes_app.route('/delete/<note>')
def delete_note(note):
    global message
    message = f"note '{note_list[note].title}' deleted"
    del note_list[note]
    save_notes()
    return redirect(url_for('display_notes'))
        