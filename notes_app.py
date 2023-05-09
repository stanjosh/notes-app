from flask import Flask, render_template, request, redirect, url_for, session, flash


notes_app = Flask(__name__.split('.')[0])
notes_app.secret_key = 'dev'
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, et cetera"


def check_for_existing(note_title):
    if note_title in session['note_dict']:
        if note_title[-1].isdigit():
            existing_title_number = int(note_title[-1]) + 1
            print(existing_title_number)
            existing_title_number = str(existing_title_number)
            print(existing_title_number)
        else:
            existing_title_number = 2
            note_title = f"{note_title.rstrip(' 0123456789')} {existing_title_number}"
    return  note_title



@notes_app.route('/')
def home(error=None):
    if error:
        flash(error)
    if not 'email' in session:
        flash('please log in')
        return redirect(url_for('login'))
    return render_template('notes.html')
    

@notes_app.route('/add')    
def new_note():
    new_note = ('New note')
    session['note_dict'][new_note] = lorem
    session.modified = True
    return redirect(url_for('home'))

@notes_app.route('/delete/<note_to_delete>')
def delete_note(note_to_delete=None):
    if note_to_delete:
        print(f"trying to delete '{session['note_dict'].pop(note_to_delete)}")
        flash(f"deleted {note_to_delete}")
        session.modified = True
    return redirect(url_for('home'))


@notes_app.route('/save/<note_title>')
def note_to_save(note_title):    
    note_title = check_for_existing(request.args.get('title'))
    content = request.args.get('content')
    session['note_dict'][note_title] = content
    session.modified = True
    return redirect(url_for('home'))

@notes_app.route('/reset')
def reset_notes():
    session['note_dict'] = {}
    session.modified = True
    flash('reset notes')
    return redirect(url_for('logout'))

@notes_app.route('/debug')
def debug_info():
    flash(str(session))
    return redirect(url_for('home'))

@notes_app.route('/login')  
def login():
    return render_template("login.html")  
 
@notes_app.route('/success', methods=["POST"])  
def success():  
    if request.method == "POST":  
        session['email'] = request.form['email']
        print(session['email'])
        session.modified = True
        flash('You were successfully logged in')
        if 'note_dict' in session:
            return redirect(url_for('home'))  
        else:
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
