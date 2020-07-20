from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plugins.db'
db = SQLAlchemy(app)


class PluginsUsed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return str(self.name)

class PluginsNotUsed(db.Model):
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

    pluginList = PluginsUsed.query.all()
    return render_template('ConfigManager.html',pluginList=pluginList)

@app.route('/PluginPage/')
def PluginPage():

    pluginList = PluginsNotUsed.query.all()
    return render_template('PluginPage.html',pluginList=pluginList)


@app.route('/delete/<int:id>')
def delete(id):

    selectedPlugin = PluginsUsed.query.get_or_404(id)
    selected_id = selectedPlugin.id
    selected_name = selectedPlugin.name

    oldPlugin = PluginsNotUsed(id=selected_id, name=selected_name)
    db.session.add(oldPlugin)
    db.session.delete(selectedPlugin)
    db.session.commit()

    return redirect('/ConfigManager/')

@app.route('/add/<int:id>')
def add(id):

    selectedPlugin = PluginsNotUsed.query.get_or_404(id)
    selected_id = selectedPlugin.id
    selected_name = selectedPlugin.name

    oldPlugin = PluginsUsed(id=selected_id, name=selected_name)
    db.session.add(oldPlugin)
    db.session.delete(selectedPlugin)
    db.session.commit()

    return redirect('/PluginPage/')

if __name__ == "__main__":
    app.run(debug=True)
