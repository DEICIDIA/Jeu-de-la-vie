import webbrowser
from flask import Flask, Response, request, render_template, jsonify
import numpy as np  
import main

app = Flask(__name__)

task = False

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
    global task
    
    if task is False:
        matrice2 = request.args.get('matrice', default = '')
        hauteur = int(request.args.get('hauteur', default = ''))
        largeur = int(request.args.get('largeur', default = ''))
        task = True

    matrice = str_mat(matrice2, hauteur, largeur)
    new_matrice = main.nextStep(matrice)
    string = ""
    for i in range(largeur):
        for j in range(hauteur):
            string += str(new_matrice[i][j]) 
    

    return string



app.run(debug = True)