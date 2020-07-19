from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/NewOrExisting/')
def NewOrExisting():
    return render_template('NewOrExisting.html')

@app.route('/FilePathEntry/')
def FilePathEntry():
    return render_template('FilePathEntry.html')

@app.route('/ConfigManager/')
def ConfigManager():
    return render_template('ConfigManager.html')

if __name__ == "__main__":
    app.run(debug=True)
