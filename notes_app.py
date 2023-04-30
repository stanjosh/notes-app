from flask import Flask, render_template, request, redirect, url_for
import os, pickle

notes_app = Flask(__name__.split('.')[0])
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, et cetera"
note_dict = {}
notes_file = os.path.join('.', "saved_notes.bin") 
notes_status = None
message = None


@notes_app.route('/')
def home():
    global message
    status = message
    message = None
    print(note_dict)
    if not note_dict:
        reset_notes()
    return render_template('notes.html', notes_to_display=display_notes(), message=status)
    
    
@notes_app.route('/edit')
@notes_app.route('/edit/<note_to_edit>')
@notes_app.route('/edit/save/<note_to_save>')
def edit_note(note_to_edit=None, note_to_save=None):
    if note_to_save:
        note = get_note_by_title(note_to_save)
        new_title = request.args.get('title', None)
        new_content = request.args.get('content', None)
        Notes.edit(note, new_title, new_content)

    if note_to_edit:
        note_to_edit = get_note_by_title(note_to_edit)
        return render_template('edit.html', note=note_to_edit)
    return redirect(url_for('home'))

@notes_app.route('/reset')
def reset():
    reset_notes()
    return redirect(url_for('home'))


@notes_app.route('/add')
def add_note():
    note_title = add()
    return redirect(url_for('edit_note', note_to_edit=note_title))


@notes_app.route('/delete/<note_title>')
def delete_note(note_title):
    delete_note(note_title)
    return redirect(url_for('home'))


def display_notes():
    return list(note_dict.values())
    
def get_note_by_title(title):
    return note_dict[title]

def check_for_existing(note_title):
    existing_titles = list(note for note in display_notes() if note.title.startswith(note_title))
    title_number = len(existing_titles)
    print(title_number)
    return  f"{note_title} {title_number + 1}" if title_number >= 1 else note_title
    

def update_note_dict_key(note, old_title=None):
    note_dict[note.title] = note
    if old_title:
        delete_note(old_title)
    save_notes()
    print (note_dict)


class Notes:
    def __init__(self, title='', content='', **kwargs):
        self.title = title
        self.content = content

    def edit(self, title, content):
        old_title = self.title
        print (f'old: {old_title}')
        self.title = title
        print (f'new: {self.title}')
        self.content = content
        print (f'new: {self.content}')
        if not old_title == self.title:
            self.title = check_for_existing(self.title)
            update_note_dict_key(note=self, old_title=old_title)
        else:
            update_note_dict_key(note=self)



def add(note_title='New Note', content=lorem):
    new_note = Notes(check_for_existing(note_title), content)
    update_note_dict_key(note=new_note)
    return new_note.title

       
def delete_note(note_title):
    del note_dict[note_title]
    save_notes()
    print(note_dict)
    
def save_notes():
    global notes_status
    with open(notes_file, "wb+") as pickle_file:
        pickle.dump(note_dict, pickle_file)
    notes_status = f"notes saved"
    
def load_notes():
    global notes_status
    global note_dict
    with open(notes_file, "rb+") as pickle_file:
        note_dict = pickle.load(pickle_file)
    notes_status = f"notes loaded"
    
def reset_notes():
    note_dict.clear()
    add('reset notes!')
    print('reset notes')
    with open(notes_file, "wb+") as pickle_file:
        pickle.dump(note_dict, pickle_file)