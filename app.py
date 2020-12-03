import webbrowser
from flask import Flask, Response, request, render_template, jsonify

app = Flask(__name__)
matrice = [[1, 0, 1], [0, 0, 1], [1, 0, 0]]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():

    reponse = app.response_class(matrice, status = 200)
    return reponse 


app.run(debug = True)