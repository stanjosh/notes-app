from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route('/<name>')
def hello(name=None):
    user = escape(name)
    return render_template('home.html', name=user)
    
if __name__ == "__main__":
    app.run()
    