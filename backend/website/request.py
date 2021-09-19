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
# API for adding Data to JSON files

# add new Guess data to JSON
@myrequest.route('/guess/add', methods=['POST'])
def addGuess():
    question = request.form.get('question')
    answer = request.form.get('answer')
    funfact = request.form.get('funfact')
    json_file_path = "website/data/guess.json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            events = json.load(f)
            event = max(events['data'], key=lambda ev: ev['id'])
            nextId = event['id'] + 1

            newGuess = {"id": nextId, "question": question, "answer": answer, "funfact": funfact}
            events['data'].append(newGuess)
            try:
                with open(json_file_path, 'w', encoding='utf-8') as fp:
                    json.dump(events, fp, sort_keys=True, indent=4, ensure_ascii=False)
                    flash('New Guess question was added.', category='success')
                    return redirect(url_for('views.addData'))

            except FileNotFoundError:
                flash("File not found. Check the path variable and filename.", category='error')
                return redirect(url_for('views.addData'))

    except FileNotFoundError:
        flash("File not found. Check the path variable and filename.", category='error')
        return redirect(url_for('views.addData'))


# add new Two Idiots data to JSON
@myrequest.route('/two-idiots/add', methods=['POST'])
def addTwoIdiots():
    category = request.form.get('category')

    json_file_path = "website/data/two-idiots.json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            events = json.load(f)
            event = max(events['data'], key=lambda ev: ev['id'])
            nextId = event['id'] + 1

            newTwoIdiots = {"id": nextId, "category": category}
            events['data'].append(newTwoIdiots)
            try:
                with open(json_file_path, 'w', encoding='utf-8') as fp:
                    json.dump(events, fp, sort_keys=True, indent=4, ensure_ascii=False)
                    flash('New Two Idiots category was added.', category='success')
                    return redirect(url_for('views.addData'))


            except FileNotFoundError:
                flash("File not found. Check the path variable and filename.", category='error')
                return redirect(url_for('views.addData'))

    except FileNotFoundError:
        flash("File not found. Check the path variable and filename.", category='error')
        return redirect(url_for('views.addData'))


# add new Two Idiots data to JSON
@myrequest.route('/different-word/add', methods=['POST'])
def addDifferentWord():
    category = request.form.get('category')

    json_file_path = "website/data/different-word.json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            events = json.load(f)
            event = max(events['data'], key=lambda ev: ev['id'])
            nextId = event['id'] + 1

            newTwoIdiots = {"id": nextId, "category": category}
            events['data'].append(newTwoIdiots)
            try:
                with open(json_file_path, 'w', encoding='utf-8') as fp:
                    json.dump(events, fp, sort_keys=True, indent=4, ensure_ascii=False)
                    flash('New Two Idiots category was added.', category='success')
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
        file_path = "website/data/"
        json_file_path = file_path + game + ".json"

    # production server, use files from docker directory 
    elif config.get('SERVER', 'modus') == "prod":
        file_path = "/app/backend/website/data/"
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
        file_path = "website/data/"
        json_file_path = file_path + game + ".json"

    # production server, use files from docker directory 
    elif config.get('SERVER', 'modus') == "prod":
        file_path = "/app/backend/website/data/"
        json_file_path = file_path + game + ".json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["objectStructure"]

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error": "cannot open file"}
