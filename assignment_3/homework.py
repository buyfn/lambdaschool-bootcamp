from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/enternew')
def enternew():
    return render_template('food.html')


@app.route('/addfood', methods = ['POST'])
def addfood():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        food = (request.form['name'],
                request.form['calories'],
                request.form['cuisine'],
                request.form['is_vegetarian'],
                request.form['is_gluten_free'])
        cursor.execute('INSERT INTO foods VALUES (?, ?, ?, ?, ?)', food)
        connection.commit()
        msg = 'completed with success'
    except:
        connection.rollback()
        msg = 'failed'
    finally:
        connection.close()
        return render_template('result.html', message = msg)


@app.route('/favorite')
def favorite():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    q = 'SELECT * FROM foods WHERE name="bread"'
    cursor.execute(q)
    res = cursor.fetchone()
    connection.close()

    return jsonify(res)


@app.route('/search')
def search():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    searchWord = request.args.get('name')
    cursor.execute('SELECT * FROM foods WHERE name=?', (searchWord, ))
    res = cursor.fetchall()
    connection.close()

    return jsonify(res)


@app.route('/drop')
def drop():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE foods')
    connection.close()

    return 'dropped'

