from flask import Flask
from notes_app import notes_app as notes_app

if __name__ == "__main__":
   notes_app.run(host='0.0.0.0', port=5000)