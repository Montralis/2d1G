from . import db


class schaetzen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frage = db.Column(db.String(10000))
    Antwort = db.Column(db.String(10000))
    fun_fact = db.Column(db.String(10000))


