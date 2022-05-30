from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/v1/square/<int:value>')
def show_user_profile(value):
    square = value * value
    return jsonify(value=value, square=square)

@app.route('/')
def hello():
    return render_template('index.htm')