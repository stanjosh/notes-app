from genericpath import exists
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
import users

app = Flask(__name__)



@app.route("/")
def hello(name=None):
    name = escape(name)
    return render_template('home.html', name=name)

@app.route('/users')
def display_profile():
    current_user = request.args.get('username')
    if current_user:
        return render_template('profile.html', user=users.get_user(current_user))
    else:
        redirect(url_for('hello'))

@app.route('/create')
def new_user():
    
    current_user = users.add_user(request.args.get('username'), request.args.get('name'), request.args.get('phone'), request.args.get('state'))
    
    print(f'created {current_user.username}')
    return redirect(url_for('display_profile', username=current_user.username))



if __name__ == "__main__":
    app.run()
    