from . import db


class schaetzen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frage = db.Column(db.String(1000))
    antwort = db.Column(db.String(2000))
    fun_fact = db.Column(db.String(2000))

class two_idiots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categorie = db.Column(db.String(100))

