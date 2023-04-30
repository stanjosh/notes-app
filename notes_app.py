from flask import Flask, render_template, request, redirect, url_for
import notes

notes_app = Flask(__name__.split('.')[0])

message = None


@notes_app.route('/')
def home():
    global message
    status = message
    message = None
    print(notes.note_dict)
    if not notes.note_dict:
        reset_notes()
    return render_template('notes.html', notes_to_display=notes.display_notes(), message=status)
    
    
@notes_app.route('/edit')
@notes_app.route('/edit/<note_to_edit>')
@notes_app.route('/edit/save/<note_to_save>')
def edit_note(note_to_edit=None, note_to_save=None):
    if note_to_save:
        note = notes.get_note_by_title(note_to_save)
        new_title = request.args.get('title', None)
        new_content = request.args.get('content', None)
        notes.Notes.edit(note, new_title, new_content)

    if note_to_edit:
        note_to_edit = notes.get_note_by_title(note_to_edit)
        return render_template('edit.html', note=note_to_edit)
    return redirect(url_for('home'))


@notes_app.route('/add')
def add_note():
    note_title = notes.add()
    return redirect(url_for('edit_note', note_to_edit=note_title))


@notes_app.route('/delete/<note_title>')
def delete_note(note_title):
    notes.delete_note(note_title)
    return redirect(url_for('home'))

        
@notes_app.route('/reset')
def reset_notes():
    notes.reset_notes()
    return redirect(url_for('home'))


@notes_app.route('/save')
def save_notes():
    notes.save_notes()
    return redirect(url_for('home'))

                    
@notes_app.route('/load') 
def load_notes():
    notes.load_notes()
    return redirect(url_for('home'))
