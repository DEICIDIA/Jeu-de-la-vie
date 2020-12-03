import webbrowser
from flask import Flask, Response, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug = True)