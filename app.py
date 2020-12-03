import webbrowser
from flask import Flask, Response, request, render_template, jsonify
import numpy as np  

app = Flask(__name__)

def str_mat(str, hauteur, largeur):
    tab = [[0]* hauteur] * largeur

    print(str)

    index_str = 0

    for i in range(largeur):
        for j in range(hauteur):

            tab[i][j] = str[index_str]
            index_str += 1


    print(tab)
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():

    matrice2 = request.args.get('matrice', default = '')
    hauteur = int(request.args.get('hauteur', default = ''))
    largeur = int(request.args.get('largeur', default = ''))

    str_mat(matrice2, hauteur, largeur)

    return "nan"


app.run(debug = True)