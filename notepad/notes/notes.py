

class Notes:
    def __init__(self, title='', content='', **kwargs) -> None:
        self.title = title
        self.content = content
        self.editing = kwargs.get('editing', False)

def add(note_list, title='Notes', content='Type some notes here.'):
    
    if not title in note_list:
        new_note = Notes(title, content, editing=True)
        note_list[new_note.title] = new_note
        return new_note.title
    else:
        note_list[title].content = content

def edit(note_list, title, content):
    if title and title in note_list:
        note_list[title].content = content
    if title and title not in note_list:
        old_title = title
        note_list[title].content = content
        
    