from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = os.environ['MYSQL_DATABASE']
app.config['MYSQL_HOST'] = os.environ['MYSQL_DB_HOST']

db  = MySQL(app)

### Temporary database
### We will replace this dictionary
@app.route('/', methods=['POST', 'GET'])
def login():
    cursor = db.connection.cursor()
    if request.method == 'GET':
        return render_template('form.html', title='Sign In')
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        status = cursor.execute('''SELECT username FROM `users` WHERE `username`="{0}" and `password`="{1}"'''.format(username,password))
        if status:
            return "<h1>Hi {0}, You are successfully logged in.</h1>".format(username)
        else:
            return " <h2>Wrong Credentials! Please <a href=\'/\'>try again</a></h2>"