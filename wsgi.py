from notes_app import notes_app
from flask import Flask


app = notes_app
app.secret_key='dev'

if __name__ == "__main__":
   app.run(host='0.0.0.0')
