from flask import (
    Flask, render_template, request, jsonify, make_response
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import hashlib
import jwt
from functools import wraps
import os

from models.index import User
from question import Question
from conn.db_utils import add_instance, delete_instance, get_all, edit_instance, commit_changes
from conn.index import create_app
from auth.user import decode_jwt_to_user, encode_user_to_jwt, get_schoolNumber

app = create_app()
secret_key = os.getenv('SECRET_KEY')
app.config["SECRET_KEY"] = secret_key
app.config["JSON_AS_ASCII"] = False

question = Question()


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return make_response(jsonify({"status": "fail", "message": "A valid token is missing!"}), 401)
        try:
            current_user = decode_jwt_to_user(token, app.config["SECRET_KEY"])
        except:
            return make_response(jsonify({"status": "fail", "message": "Invalid Token"}), 401)

        return func(current_user, *args, **kwargs)

    return decorated


@app.route("/question/<id>", methods=["GET", "POST"])
@token_required
def question_api(auth_user, id):
    id = int(id)

    if request.method == "GET":
        # RETURN QUESTION
        target_question = question[id]

        print(target_question)

        return jsonify(target_question)

    # POST TYPE
    # QUESTION NUMBER 1~
    # ANSWER INDEX 1~
    elif request.method == "POST":
        # SAVE THE DICTIONARY
        params = request.get_json()

        # /question/1 {answer_idx: 2}
        answer_idx = int(params.get("answer_idx"))

        if answer_idx == None:
            return make_response(jsonify({"status": "fail", "message": "Please Send the Question Answer Index."}), 401)

        # GET Question From Module
        answer, type = question.get(id, answer_idx)

        if answer == None and type == None:
            return make_response(jsonify({"status": "fail", "message": "Please Send Appropirate Answer Index"}), 401)

        schoolNumber = auth_user.get("schoolNumber")

        # TODO: Save the answer to DB
        instance = User.query.filter_by(schoolNumber=schoolNumber).first_or_404(
            description='There is no user with {}. Please Login First.'.format(schoolNumber))
        setattr(instance, type, answer)
        commit_changes()

        return jsonify({"status": "success", "message": "Save your answer to the server successfully"})


@app.route("/create_user", methods=["POST"])
def post():
    print(request.args.get('user'))

    params = request.get_json()

    #username = params.get('username')
    password = params.get('password')
    schoolNumber = params.get('schoolNumber')

    # hashed_password = bcrypt.hashpw(password, salt)
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    # TODO: Create USER Row
    add_instance(User,
                 password=hashed_password, schoolNumber=schoolNumber)

    encoded_jwt_token = encode_user_to_jwt(
        schoolNumber, hashed_password, app.config["SECRET_KEY"])

    return jsonify({"status": "success", "message": "Create user successfully", "Authorization": encoded_jwt_token}), 200


@app.route("/login", methods=["POST"])
def login():
    params = request.get_json()

    # Without JWT Token
    schoolNumber = params.get('schoolNumber')
    password = params.get('password')

    # hashed_user_password = bcrypt.hashpw(password, salt)
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    # GET Hashed password from Database using Username
    target_user = User.query.filter(User.schoolNumber == schoolNumber).first_or_404(
        description='There is no user with {}'.format(schoolNumber))

    # if not target_user:
    #     return jsonify({"status": "fail", "message": "No user found."})
    database_password = target_user.password

    if hashed_password == database_password:
        # Login
        encoded_jwt_token = encode_user_to_jwt(
            schoolNumber, hashed_password, app.config["SECRET_KEY"])

        return jsonify({"status": "success", "message": "Login successfully!", "Authorization": encoded_jwt_token}), 200

    else:
        return jsonify({"status": "fail", "message": "Password is wrong."}), 404


# @app.route("/valid", methods=["GET"])
# def jwt_valid():
#     header = request.headers.get('Authorization')

#     if header == None:
#         return jsonify({"status": "fail", "message": "Please Login First"}), 404

#     data = decode_jwt_to_user(header)
#     return data, 200


@app.route("/users", methods=["GET"])
@token_required
def user_list(auth):
    users = get_all(User)
    all_users = []
    for user in users:
        new_user = {
            "id": user.id,
            "password": user.password,
            "gender": user.gender,
            "mbti": user.mbti,
            "bloodtype": user.bloodtype,
            "favoriteFood": user.favoriteFood,
            "favoriveColor": user.favoriteColor,
        }

        all_users.append(new_user)

    return jsonify(all_users), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port="4000", debug=True)
