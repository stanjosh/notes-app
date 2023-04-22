

class Notes:
    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content

def add_note(note_list, title, content):
    
    if not title in note_list:
        new_note = Notes(title, content)
        note_list[new_note.title] = new_note
    else:   
        note_list[title].content = content


        