from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class HorseRace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race_name = db.Column(db.String(120), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class Bet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('horse_race.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    selected_horse = db.Column(db.String(120), nullable=False)
