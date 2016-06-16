from flask import Flask, render_template, request, jsonify, url_for
import json
from random import choice
from collections import defaultdict
import os
app = Flask(__name__)


names = defaultdict(list)
path = os.path.dirname(__file__) + "/adjectives.txt"
with open(path, "r") as f:
    adjectives = [line.strip() for line in f]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greeting", methods=["POST"])
def greeting():

    json = request.json
    name = json["name"]
    # name = request.data["name"]
    if name not in names:
        names[name] = choice(adjectives)

    greeting = "Рад тебя видеть снова, " + names[name] + " " + name + "!"
    # return jsonify({"name":name, "greeting":greeting})
    return greeting

if __name__ == "__main__":
    app.run(debug=True)

