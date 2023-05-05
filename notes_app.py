from flask import Flask, render_template, request, redirect, url_for, session


notes_app = Flask(__name__.split('.')[0])
notes_app.secret_key = 'dev'


@notes_app.route('/')
def home():
    if not session['email']:
        return redirect(url_for('login'))
    if not session['note_dict']:
        return redirect(url_for('reset_notes'))
    return render_template('notes.html')
    
@notes_app.route('/add')    
@notes_app.route('/edit/<note_to_edit>')
@notes_app.route('/delete/<note_to_delete>')
def edit_note(note_to_edit='New note', note_to_delete=None):
    if note_to_delete:
        session['note_dict'].pop(note_to_delete)
        session.modified = True
        return redirect(url_for('home'))
    return render_template('edit.html', note_to_edit=note_to_edit)

@notes_app.route('/edit/save')
def note_to_save():
    edit(request.args.get('title'), request.args.get('content'))
    session.modified = True
    return redirect(url_for('home'))

@notes_app.route('/reset')
def reset_notes():
    session['note_dict'] = {}
    session['note_dict']['reset notes!'] = lorem
    session.modified = True
    return redirect(url_for('login'))

@notes_app.route('/debug')
def debug_info():
    print(session)
    return redirect(url_for('home'))

@notes_app.route('/login')  
def login():
    return render_template("login.html")  
 
@notes_app.route('/success', methods=["POST"])  
def success():  
    if request.method == "POST":  
        session['email']=request.form['email']
        print(session['email'])
        session.modified = True
        try:
            if session['note_dict']:
                return redirect(url_for('home', message='successfully logged in'))  
        except KeyError:
            return redirect(url_for('reset_notes'))

    
 
@notes_app.route('/logout')  
def logout():  
    if 'email' in session:  
        session.pop('email')
        session.modified = True
        print(session)
        return redirect(url_for('home', message='successfully logged out'))
    else:  
        return '<p>user already logged out</p>'  


lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, et cetera"

def delete(title):
    return session['note_dict'].pop(title)

def edit(title='New Note', content=lorem):
    title = check_for_existing(title)
    session['note_dict'][title] = content


def check_for_existing(note_title):
    existing_title_number = len(list(note for note in session['note_dict'] if note.startswith(note_title)))
    return  f"{note_title} {existing_title_number + 1}" if existing_title_number >= 1 else note_title



def save(note_dict):
    # with open(os.path.join('./static', "saved_notes.bin") , "wb+") as pickle_file:
    #     pickle.dump(session['note_note_dict'], pickle_file)
    pass