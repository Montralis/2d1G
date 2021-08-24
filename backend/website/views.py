from flask import Blueprint, render_template
from faker import Faker
from .models import two_idiots
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    fill_database()
    return render_template("home.html")



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
