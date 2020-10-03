import os
from flask import Flask, render_template, jsonify


template_dir = os.path.relpath('../templates')
app = Flask(__name__, template_folder=template_dir)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


