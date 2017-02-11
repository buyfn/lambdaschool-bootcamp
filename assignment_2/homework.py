from flask import Flask, render_template, jsonify
app = Flask(__name__)

# 1
# @app.route('/')
# def index():
#     return 'hello, worlds!'

# 2
@app.route('/birthday')
def birthday():
    return 'February 4 1946'

# 3
@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name

# 4
@app.route('/')
def index():
    return render_template('home.html')


# Extra credit

# 1
@app.route('/sum/<augend>/<addend>')
def add(augend, addend):
    return str(int(augend) + int(addend))

# 2
@app.route('/multiply/<multiplier>/<multiplicand>')
def multiply(multiplier, multiplicand):
    return str(int(multiplier) * int(multiplicand))

@app.route('/substract/<minuend>/<subtrahend>')
def substract(minuend, subtrahend):
    return str(int(minuend) - int(subtrahend))

# 3
@app.route('/favoritefoods')
def favoritefoods():
    foodlist = ['meat', 'bread', 'hummus']
    return jsonify(foodlist)

