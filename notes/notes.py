

class Notes:
    def __init__(self, title='', content='', **kwargs) -> None:
        self.title = title
        self.content = content
        self.editing = kwargs.get('editing', False)

def add(note_list, title='Notes', content='Type some notes here.'):
    new_note = Notes(title, content, editing=True)
    note_list[new_note.title] = new_note
    return new_note


def edit(note_list, note, title, content):
    if title in note_list:
        note.content = content
    else:
        old_title = note.title
        note.title = title
        note_list[title]= note
        del note_list[old_title]
        
        
    