from flask import Blueprint, request, jsonify
from .models import db, User, HorseRace, Bet

bp = Blueprint('main', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/races', methods=['GET'])
def get_races():
    races = HorseRace.query.all()
    return jsonify([race.to_dict() for race in races]), 200

@bp.route('/bets', methods=['POST'])
def place_bet():
    data = request.get_json()
    new_bet = Bet(user_id=data['user_id'], race_id=data['race_id'], amount=data['amount'], selected_horse=data['selected_horse'])
    db.session.add(new_bet)
    db.session.commit()
    return jsonify({'message': 'Bet placed successfully'}), 201

def init_app(app):
    app.register_blueprint(bp)
