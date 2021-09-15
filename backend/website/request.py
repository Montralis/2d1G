import flask
import json
import random
from os import path
from flask import Blueprint, jsonify


request = Blueprint('request', __name__)


# returns the Flask version
@request.route('/version', methods=['GET'])
def version():
    return jsonify(flask.__version__)


# routes for game: Guess

# returns a shuffled list of guess questions | return == array
@request.route('/guess', methods=['GET'])
def guess():
    json_file_path = "website/data/guess.json"

    try:
        with open(json_file_path, "r") as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["data"]
            random.shuffle(dataDict)

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error" : "cannot open file"}


# returns the structure of a guess object | return == JSON
@request.route('/guess/structure', methods=['GET'])
def guessStructure():
    json_file_path = "website/data/guess.json"

    try:
        with open(json_file_path, "r") as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["objectStructure"]

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error" : "cannot open file"}


# routes for game: TwoIdiots

# returns a shuffled list of twoIdiots questions | return == array
@request.route('/two-idiots', methods=['GET'])
def twoIdiots():
    json_file_path = "website/data/twoIdiots.json"

    try:
        with open(json_file_path, "r") as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["data"]
            random.shuffle(dataDict)

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error" : "cannot open file"}


# returns the structure of a twoIdiots object | return == JSON
@request.route('/two-idiots/structure', methods=['GET'])
def twoIdiotsStructure():
    json_file_path = "website/data/twoIdiots.json"

    try:
        with open(json_file_path, "r") as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["objectStructure"]

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error" : "cannot open file"}
