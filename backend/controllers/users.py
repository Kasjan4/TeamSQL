from flask import Blueprint, request
from models.user import User
from serializers.user import UserSchema


user_schema = UserSchema()

router = Blueprint(__name__, 'users')


@router.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data['email']).first()

    if not user:
        return {'message': 'Unauthorized'}, 200

    if not user.validate_password(data['password']):
        return {'message': 'Unauthorized'}, 402

    token = user.generate_token()

    return {'token': token, 'message': 'Welcome back'}


# @router.route('/users/<int:id>', methods=['GET'])
# def get_single_user(id):

#     user = User.query.get(id)

#     if not user:
#         return {'message': 'User not available'}, 404

#     return user_schema.jsonify(user), 200


@router.route('/users/<string:comp>', methods=['GET'])
def get_users(comp):
    print(comp, flush=True)

    if comp == 'All':
        users = User.query.all()
        return user_schema.jsonify(users, many=True), 200

    else:
        users = User.query.filter_by(company=comp)
        return user_schema.jsonify(users, many=True), 200
