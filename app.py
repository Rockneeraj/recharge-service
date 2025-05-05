from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# SQLite DB configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(BASE_DIR, 'db')
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

db_path = os.path.join(db_dir, 'recharge.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Recharge model
class Recharge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    plan_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="SUCCESS")

# Create tables
with app.app_context():
    db.create_all()

@app.route('/recharges', methods=['POST'])
def create_recharge():
    data = request.json
    user_id = data.get('user_id')
    plan_id = data.get('plan_id')
    new_recharge = Recharge(user_id=user_id, plan_id=plan_id)
    db.session.add(new_recharge)
    db.session.commit()
    return jsonify({'message': 'Recharge successful', 'recharge_id': new_recharge.id}), 201

@app.route('/recharges', methods=['GET'])
def list_recharges():
    recharges = Recharge.query.all()
    result = [{'id': r.id, 'user_id': r.user_id, 'plan_id': r.plan_id, 'status': r.status} for r in recharges]
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

