from . import db
from dataclasses import dataclass


@dataclass
class schaetzen(db.Model):
    __tablename__ = 'schaetzen'
    id: int
    frage: str
    antwort: str
    fun_fact: str

    id = db.Column(db.Integer, primary_key=True)
    frage = db.Column(db.String(1000))
    antwort = db.Column(db.String(2000))
    fun_fact = db.Column(db.String(2000))
    
@dataclass
class two_idiots(db.Model):
    id: int
    categorie: str

    id = db.Column(db.Integer, primary_key=True)
    categorie = db.Column(db.String(100))

