from flask import Blueprint, render_template, request, flash
from faker import Faker
from .models import schaetzen, two_idiots
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")



@views.route('/addguess', methods=['GET', 'POST'])
def addguess():
    if request.method == 'POST':
        antwort = request.form.get('antwort')
        frage = request.form.get('frage')

        if len(frage)< 1:
            flash('Keine Frage eingetragen', category='error')
        elif len(antwort) < 1:
            flash('Keine Antwort eingetragen', category='error')
        else:
            new_schaetzen = schaetzen(frage = frage, antwort = antwort)
            db.session.add(new_schaetzen)
            db.session.commit()
            flash('Frage added!', category='success')

    return render_template("addguess.html")

@views.route('/addtwoiditos', methods=['GET', 'POST'])
def addtwoiditos():
    if request.method == 'POST':
        categorie = request.form.get('categorie')

        if len(categorie)< 1:
            flash('Keine Kategorie eingetragen', category='error')

        else:
            new_two = two_idiots(categorie = categorie)
            db.session.add(new_two)
            db.session.commit()
            flash('Frage added!', category='success')

    return render_template("addtwoidiots.html")