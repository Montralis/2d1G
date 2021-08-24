from flask import Blueprint

request = Blueprint('request', __name__)


@request.route('/test', methods=['GET', 'POST'])
def home():
    return {1:"sdfds"}
