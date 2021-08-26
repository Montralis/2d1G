from sqlalchemy.sql.expression import select
from .models import schaetzen, two_idiots
from flask import Blueprint, jsonify
from  sqlalchemy.sql.expression import func, select
from . import db


request = Blueprint('request', __name__)


def fill_database():

    from website.models import schaetzen, two_idiots
    from faker import Faker
    faker = Faker()

    for i in range(1,100):
        spiel1 = schaetzen(frage = faker.text(max_nb_chars=80), antwort = faker.text(max_nb_chars=200), fun_fact = faker.text(max_nb_chars=80))
        spiel2 = two_idiots(categorie = faker.text(max_nb_chars=100))
        db.session.add(spiel1)
        db.session.add(spiel2)
    db.session.commit()

    print('Testdata were created')


@request.route('/randomSchaetzen', methods=['GET'])
def randomSchaetzen():
    # result = db.session.execute(select(schaetzen).order_by(schaetzen.id))   
    result = db.session.query(schaetzen).order_by(func.random()).first()
    print('asdasd sad asd asd asd a' ,result) 
    return jsonify({'result':result})



@request.route('/randomTwo', methods=['GET'])
def randomTwo():
    result = db.session.query(two_idiots).order_by(func.random()).first()
    print('asdasd sad asd asd asd a' ,result) 
    return jsonify({'result':result})

