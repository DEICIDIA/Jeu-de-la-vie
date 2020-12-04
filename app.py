import webbrowser
from flask import Flask, Response, request, render_template, jsonify
import numpy as np  
import main

app = Flask(__name__)

def str_mat(str, hauteur, largeur):

    tab = [[0]*hauteur for i in range(largeur)]
   
    for i in range(len(str)):
        tab[i%largeur][i//hauteur] = int(str[i])

    return tab    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():

    matrice2 = request.args.get('matrice', default = '')
    hauteur = int(request.args.get('hauteur', default = ''))
    largeur = int(request.args.get('largeur', default = ''))
    matrice = str_mat(matrice2, hauteur, largeur)
    new_matrice = main.nextStep(matrice)
    string = ""

    for j in range(hauteur):
        for i in range(largeur):
            string += str(new_matrice[i][j]) 

    return string

app.run(debug = True)