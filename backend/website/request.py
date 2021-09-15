import flask
import json
import random
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


# add new guess data to JSON
@request.route('/add-guess', methods=['POST'])
def addGuess():
    question = request.args.get('question')
    answer = request.args.get('answer')
    funfact = request.args.get('funfact')
    json_file_path = "website/data/guess.json"


    with open(json_file_path) as f:
        events = json.load(f)
        event = max(events['data'], key=lambda ev: ev['id'])
        nextId = event['id'] + 1

        print(nextId)


# routes for game: TwoIdiots

# returns a shuffled list of twoIdiots questions | return == array
@request.route('/two-idiots', methods=['GET'])
def twoIdiots():
    json_file_path = "website/data/two-idiots.json"

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
    json_file_path = "website/data/two-idiots.json"

    try:
        with open(json_file_path, "r") as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["objectStructure"]

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error" : "cannot open file"}
