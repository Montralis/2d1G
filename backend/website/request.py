import flask
import json
import random
from flask import Blueprint, jsonify, request, flash,  redirect, url_for


myrequest = Blueprint('myrequest', __name__)


# common routes

# returns the Flask version
@myrequest.route('/version', methods=['GET'])
def version():
    return jsonify(flask.__version__)


# --------------------------------------------------------------------------------------------------

# routes for game: Guess

# returns a shuffled list of Guess questions | return == array
@myrequest.route('/guess', methods=['GET'])
def guess():
    json_file_path = "website/data/guess.json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["data"]
            random.shuffle(dataDict)

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error" : "cannot open file"}


# returns the structure of a Guess object | return == JSON
@myrequest.route('/guess/structure', methods=['GET'])
def guessStructure():
    json_file_path = "website/data/guess.json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["objectStructure"]

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error" : "cannot open file"}


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

            newGuess =  {"id": nextId, "question": question, "answer": answer, "funfact": funfact}
            events['data'].append(newGuess)
            try:
                with open(json_file_path, 'w', encoding='utf-8') as fp:
                    json.dump(events, fp, sort_keys=True, indent=4, ensure_ascii=False)
                    flash('New Guess question was added.', category='success')
                    return redirect(url_for('views.addData'))

            except FileNotFoundError:
                flash("File not found. Check the path variable and filename.",  category='error')
                return redirect(url_for('views.addData'))

    except FileNotFoundError:
        flash("File not found. Check the path variable and filename.",  category='error')
        return redirect(url_for('views.addData'))


# --------------------------------------------------------------------------------------------------

# routes for game: Two Idiots

# returns a shuffled list of Two Idiots categories | return == array
@myrequest.route('/two-idiots', methods=['GET'])
def twoIdiots():
    json_file_path = "website/data/two-idiots.json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["data"]
            random.shuffle(dataDict)

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error" : "cannot open file"}


# returns the structure of a Two Idiots object | return == JSON
@myrequest.route('/two-idiots/structure', methods=['GET'])
def twoIdiotsStructure():
    json_file_path = "website/data/two-idiots.json"

    try:
        with open(json_file_path, "r", encoding='utf-8') as f:
            guessJson = json.loads(f.read())
            dataDict = guessJson["objectStructure"]

            return jsonify(dataDict)

    except FileNotFoundError:
        print("File not found. Check the path variable and filename.")
        return {"error" : "cannot open file"}


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

            newTwoIdiots =  {"id": nextId, "category": category}
            events['data'].append(newTwoIdiots)
            try:
                with open(json_file_path, 'w', encoding='utf-8') as fp:
                    json.dump(events, fp, sort_keys=True, indent=4, ensure_ascii=False)
                    flash('New Two Idiots category was added.', category='success')
                    return redirect(url_for('views.addData'))


            except FileNotFoundError:
                flash("File not found. Check the path variable and filename.",  category='error')
                return redirect(url_for('views.addData'))

    except FileNotFoundError:
        flash("File not found. Check the path variable and filename.",  category='error')
        return redirect(url_for('views.addData'))
