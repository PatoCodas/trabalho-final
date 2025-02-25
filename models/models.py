from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomePiloto = db.Column(db.String(100), nullable=False)
    tempo = db.Column(db.String(50), nullable=False)
    pista = db.Column(db.String(100), nullable=False)
