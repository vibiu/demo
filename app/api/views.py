"""Api."""
from datetime import datetime
from flask import request, jsonify, abort
from app import db
from app.models import User
from . import api


@api.route('/user', methods=['POST'])
def post_user():
    info = request.json
    username = info.get('username')
    password = info.get('password')
    if username and isinstance(username, str):
        user = User.query.filter_by(username=username).first()
    else:
        abort(400)
    if not user:
        user = User(username=username)
    user.password = password
    user.update_time = datetime.now()
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': username})


@api.route('/echo')
def echo():
    return jsonify({'message': 'hello world'})
