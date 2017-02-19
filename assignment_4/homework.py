from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/movie', methods = ['POST'])
def movie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        movieData = (request.form['name'],
                     request.form['year'],
                     request.form['rating'])
        cursor.execute('INSERT INTO movies VALUES (?, ?, ?)', movieData)
        connection.commit()
        msg = 'movie successfully added'
    except:
        connection.rollback()
        msg = 'failed to add the movie'
    finally:
        connection.close()
        return render_template('result.html', msg = msg)


@app.route('/movies')
def movies():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    q = 'SELECT * FROM movies'
    cursor.execute(q)
    res = cursor.fetchall()
    connection.close()

    return jsonify(res)


@app.route('/search')
def search():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    searchWord = request.args.get('name')
    cursor.execute('SELECT * FROM movies WHERE name=?', (searchWord, ))
    res = cursor.fetchall()
    connection.close()

    return jsonify(res)

