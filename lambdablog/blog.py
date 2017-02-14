from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')
print('Connected to db')

connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')

@app.route('/')
def index():
    return 'This is a test'

@app.route('/new')
def new_post():
    return render_template('new.html')

@app.route('/addrecord', methods = ['POST'])
def addrecord():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    print(request.form['post'])

    try:
        title = request.form['title']
        post = request.form['post']
        cursor.execute('INSERT INTO posts (title, post) VALUES (?, ?)', (title, post))
        connection.commit()
        msg = "record added"
    except:
        connection.rollback()
        msg = "error in insertion"
    finally:
        return render_template('result.html', msg = msg)
        connection.close()

