#JEU DE LA VIE

import webbrowser
from flask import Flask, Response, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')