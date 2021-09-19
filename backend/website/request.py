import os
import flask
import json
import random
from flask import Blueprint, jsonify, request, flash, redirect, url_for
import configparser


myrequest = Blueprint('myrequest', __name__)


config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'serverconf.cfg'))
print(config.get('SERVER', 'modus'))
# --------------------------------------------------------------------------------------------------
# common routes

# returns the Flask version
@myrequest.route('/version', methods=['GET'])
def version():
    return jsonify(flask.__version__)


# --------------------------------------------------------------------------------------------------
# routes for adding Data to JSON files

# add new Guess data to JSON
@myrequest.route('/add/guess', methods=['POST'])
def addGuess():
    question = request.form.get('question')
    answer = request.form.get('answer')
    funfact = request.form.get('funfact')

    newGuess = { "question": question, "answer": answer, "funfact": funfact}
    return safeToFile(newGuess, "guess")


# add new Two Idiots data to JSON
@myrequest.route('/add/two-idiots', methods=['POST'])
def addTwoIdiots():
    category = request.form.get('category')

    newTwoIdiots = { "category": category}
    return safeToFile(newTwoIdiots, "two-idiots")


# add new Two Idiots data to JSON
@myrequest.route('/add/different-word', methods=['POST'])
def addDifferentWord():
    different = request.form.get('different')
    wanted = request.form.get('wanted')

    newDifferentWord = {"wanted": wanted, "different":different} 
    return safeToFile(newDifferentWord, "different-word")


def safeToFile(jsonObject, filename ):

    # development server, use file directly 
    if config.get('SERVER', 'modus') == "dev":
        file_path = config.get('FILE_PATH', 'dev_def')
        json_file_path = file_path + filename + ".json"

    # production server, use files from docker directory 
    elif config.get('SERVER', 'modus') == "prod":
        file_path = config.get('FILE_PATH', 'prod_def')
        json_file_path = file_path + filename + ".json"


    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            events = json.load(f)
            event = max(events['data'], key=lambda ev: ev['id'])
            nextId = event['id'] + 1

            jsonObject['id'] = nextId
            events['data'].append(jsonObject)

            try:
                with open(json_file_path, 'w', encoding='utf-8') as fp:
                    json.dump(events, fp, sort_keys=True, indent=4, ensure_ascii=False)
                    flash('New' + filename + 'category was added.', category='success')
                    return redirect(url_for('views.addData'))


            except FileNotFoundError:
                flash("File not found. Check the path variable and filename.", category='error')
                return redirect(url_for('views.addData'))

    except FileNotFoundError:
        flash("File not found. Check the path variable and filename.", category='error')
        return redirect(url_for('views.addData'))



# ------------------------------------------------------------------

# returns a shuffled list of game questions | return == array
@myrequest.route('/game/<game>', methods=['GET'])
def gameData(game):

    # development server, use file directly 
    if config.get('SERVER', 'modus') == "dev":
        file_path = config.get('FILE_PATH', 'dev_def')
        json_file_path = file_path + game + ".json"

    # production server, use files from docker directory 
    elif config.get('SERVER', 'modus') == "prod":
        file_path = config.get('FILE_PATH', 'prod_def')
        json_file_path = file_path + game + ".json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["data"]
            random.shuffle(dataDict)

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error": "cannot open file"}


# returns the structure of a Guess object | return == JSON
@myrequest.route('/structure/<game>', methods=['GET'])
def gameStructure(game):

    # development server, use file directly 
    if config.get('SERVER', 'modus') == "dev":
        file_path = config.get('FILE_PATH', 'dev_def')
        json_file_path = file_path + game + ".json"

    # production server, use files from docker directory 
    elif config.get('SERVER', 'modus') == "prod":
        file_path = config.get('FILE_PATH', 'prod_def')
        json_file_path = file_path + game + ".json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["objectStructure"]

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error": "cannot open file"}
