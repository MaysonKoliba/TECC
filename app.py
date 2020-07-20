from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plugins.db'
db = SQLAlchemy(app)


class Plugin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return str(self.name)


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
