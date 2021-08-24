from faker import Faker
from .models import two_idiots
from flask import Blueprint
from . import db


request = Blueprint('request', __name__)


@request.route('/test', methods=['GET', 'POST'])
def home():

    
    return {1:"sdfds"}
