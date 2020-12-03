import webbrowser
from flask import Flask, Response, request, render_template, jsonify
import numpy as np  

app = Flask(__name__)

matrice = np.zeros((5,5))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():

    matrice2 = request.args.get('matrice', default = '')
    print(matrice2)

    return "nan"


app.run(debug = True)