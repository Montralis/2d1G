from sqlalchemy.sql.expression import select
from .models import schaetzen, two_idiots
from flask import Blueprint, jsonify
from  sqlalchemy.sql.expression import func, select
from . import db


request = Blueprint('request', __name__)


@request.route('/randomSchaetzen', methods=['GET', 'POST'])
def home():
    # result = db.session.execute(select(schaetzen).order_by(schaetzen.id))   
    result = db.session.query(schaetzen).order_by(func.random()).first()
    print('asdasd sad asd asd asd a' ,result) 
    return jsonify({'result':result})


