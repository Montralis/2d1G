from os import path
from flask import Blueprint, jsonify
import json
import random


request = Blueprint('request', __name__)

# route for Game: Guess

# returns a shuffeld list of guess questions | return == array
@request.route('/randomGuess', methods=['GET'])
def guesss():
    json_file_path = "website/data/guess.json"

    try:
        with open(json_file_path, "r") as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["data"]
            random.shuffle(dataDict)

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename")
        return {"error" : "cant open file"}


# returns the sturcture of a Guess Object | return == JSON
@request.route('/sturctureGuess', methods=['GET'])
def guesssSturcture():
    json_file_path = "website/data/guess.json"

    try:
        with open(json_file_path, "r") as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["objectStructur"]

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename")
        return {"error" : "cant open file"}


# ------------------------------------------------------------------
# route for Game: TwoIdiots


# returns a shuffeld list of twoIdiots questions | return == array
@request.route('/randomTwoIdiots', methods=['GET'])
def randomTwo():
    json_file_path = "website/data/twoIdiots.json"

    try:
        with open(json_file_path, "r") as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["data"]
            random.shuffle(dataDict)

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename")
        return {"error" : "cant open file"}


# returns the sturcture of a twoIdiots Object | return == JSON
@request.route('/sturctureTwoIdiots', methods=['GET'])
def guesssGuess():
    json_file_path = "website/data/twoIdiots.json"

    try:
        with open(json_file_path, "r") as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["objectStructur"]

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename")
        return {"error" : "cant open file"}