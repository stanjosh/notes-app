from fileinput import filename
import pickle
import os

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, et cetera"

note_dict = {}
notes_file = os.path.join('.', "saved_notes.bin") 
notes_status = None

def display_notes():
    load_notes()
    return list(note_dict.values())
    
def get_note_by_title(title):
    return note_dict[title]

def check_for_existing(note_title):
    if note_title:
        try:
            get_note_by_title(note_title)
        except KeyError:
            return note_title
    return f"New Note {len(display_notes())}"

def update_note_dict_key(note, old_title=None):
    note_dict[note.title] = note
    if old_title:
        print (f"removed dictionary entry '{note_dict.pop(old_title)}")
    print (note_dict)
    save_notes()

class Notes:
    def __init__(self, title='', content='', **kwargs):
        self.title = title
        self.content = content
        self.editing = kwargs.get('editing', False)

    def edit(self, title, content):
        old_title = self.title
        print (f'old: {old_title}')
        self.title = check_for_existing(title)
        print (f'new: {self.title}')
        self.content = content
        print (f'new: {self.content}')
        update_note_dict_key(note=self, old_title=old_title)

    
def add(title='New Note', content=lorem):
    new_note = Notes(check_for_existing(title), content, editing=True)
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
    with open(notes_file, "wb+") as pickle_file:
        pickle.dump(note_dict, pickle_file)