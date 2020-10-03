import os
from flask import Flask, render_template, jsonify
import json

basedir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.relpath("../templates")
static_dir = os.path.relpath("../static")
data_dir = os.path.join(basedir,"data")
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/team", methods=["GET"])
def team():
    f = open(os.path.join(data_dir,"team.json"),"r")
    json_obj = json.load(f)
    names = [m["name"] for m in json_obj["team"]]
    roles = [m["role"] for m in json_obj["team"]]
    imgs = [m["img"] for m in json_obj["team"]]
    about = [m["about"] for m in json_obj["team"]]
    return render_template("team.html",team=zip(names,roles,imgs,about))

