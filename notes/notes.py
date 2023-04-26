

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna \
aliqua. Ut enim ad minim veniam, quis nostrud exercitation \
ullamco laboris nisi ut aliquip ex ea commodo consequat. \
Duis aute irure dolor in reprehenderit in voluptate velit \
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint \
occaecat cupidatat non proident, sunt in culpa qui officia \
deserunt mollit anim id est laborum."

class Notes:
    def __init__(self, title='', content='', **kwargs) -> None:
        self.title = title
        self.content = content
        self.editing = kwargs.get('editing', False)

def add(note_list, title='Notes', content=lorem):
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
        
def delete(note_list, note):
    return f"note '{note_list.pop(note).title}' deleted"
    
        