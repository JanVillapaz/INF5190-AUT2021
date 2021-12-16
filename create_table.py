from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.db'

db = SQLAlchemy(app)


class Piscines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_ue = db.Column(db.Integer, primary_key=False)
    type_piscine = db.Column(db.String, nullable=False)
    nom = db.Column(db.String(120), nullable=False)
    arrondissement = db.Column(db.String(120), nullable=False)
    adresse = db.Column(db.String, nullable=True)
    propriete = db.Column(db.String(120), nullable=True)
    gestion = db.Column(db.String(120), nullable=True)
    point_x = db.Column(db.String(20), nullable=False)
    point_y = db.Column(db.String(60), nullable=False)
    equipement = db.Column(db.String(120), nullable=False)
    long = db.Column(db.String(20), nullable=False)
    lat = db.Column(db.String(20), nullable=False)
