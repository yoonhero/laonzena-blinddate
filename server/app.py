from flask import (
    Flask, render_template, request, jsonify, make_response
)
from flask_sqlalchemy import SQLAlchemy
import hashlib
import jwt
from functools import wraps
import os
import csv
import pandas as pd
import json
from flask_cors import CORS, cross_origin
from sqlalchemy.exc import IntegrityError

from database.index import db
from models.index import User, Message, Room
from question import Question
from conn.db_utils import add_instance, delete_instance, get_all, edit_instance, commit_changes
from conn.index import create_app
from auth.user import decode_jwt_to_user, encode_user_to_jwt, get_schoolNumber
from ml.index import RecommendSystem

app = create_app()
secret_key = os.getenv('SECRET_KEY')
app.config["SECRET_KEY"] = secret_key
app.config["JSON_AS_ASCII"] = False

cors = CORS(app, resources={r'*': {'origins': '*'}})

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


def user_list(auth, save_csv):
    secretUser = os.getenv("SECRET_USER")
    # if auth.get("schoolNumber") != secretUser:
    #     return make_response(jsonify({"status": "faile", "message": "No Access Authority"}), 401)

    users = get_all(User)
    all_users = []
    for user in users:
        new_user = {
            "schoolNumber": user.schoolNumber,
            "gender": user.gender,
            "age": user.age,
            "mbti": user.mbti,
            "bloodtype": user.bloodtype,
            "favoriteFood": user.favoriteFood,
            "favoriveColor": user.favoriteColor,
            "matchedUser": user.matchedUser,
            "matched": user.matched,
        }

        all_users.append(new_user)

    all_users = pd.DataFrame(all_users).reset_index(drop=True)

    if bool(save_csv):
        # with open('users.csv', 'wb') as f:
        #     to_save_data = all_users.iloc[:, :-2]
        #     w = csv.writer(f)
        #     w.writerow(to_save_data.keys())
        #     w.writerow(to_save_data.values())
        all_users.to_csv("./users.csv")

    return all_users


@app.route("/question/<id>", methods=["GET", "POST"])
@token_required
def question_api(auth_user, id):
    id = int(id)

    if request.method == "GET":
        # RETURN QUESTION
        target_question = question[id]

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
def create_user():
    params = request.get_json()

    #username = params.get('username')
    password = params.get('password')
    schoolNumber = params.get('schoolNumber')

    # hashed_password = bcrypt.hashpw(password, salt)
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    # TODO: Create USER Row
    # add_instance(User,
    #              )

    instance = User.query.filter(User.schoolNumber == schoolNumber).first()
    if instance:
        return jsonify({"status": "fail", "message": "User is already existed"}, 401)

    instance = User(password=hashed_password, schoolNumber=schoolNumber)
    db.session.add(instance)
    db.session.commit()

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


@app.route("/matching", methods=["POST", "GET"])
@token_required
def matching(auth):
    params = request.get_json()
    save_csv = params.get('save_csv')

    users = user_list(auth, bool(int(save_csv)))
    secretUser = os.getenv("SECRET_USER")

    if request.method == "GET":
        print(users)
        users_dict = users.to_dict()

        if auth.get("schoolNumber") == secretUser:
            return make_response(jsonify({"status": "success", "users": users_dict}), 200)

        print(users_dict.get("schoolNumber"))
        userIdx = list(users_dict.get("schoolNumber").values()).index(
            auth.get("schoolNumber"))

        # user_dict = users_dict
        print(userIdx)

        return make_response(jsonify({"status": "success", "matched": users_dict.get("matched").get(str(userIdx))}), 200)

    elif request.method == "POST":
        if auth.get("schoolNumber") != secretUser:
            return make_response(jsonify({"status": "faile", "message": "No Access Authority"}), 401)

        # Matching is only for unmatched people
        all_user = users.loc[users.matched == False]
        all_user = all_user.iloc[:, :-2]  # Cleaned Dataframe for prediction

        if all_user.empty:
            return make_response(jsonify({"status": "fail", "message": "No user to match"}), 401)

        recommendSystem = RecommendSystem(all_user)

        recommendSystem.recommend("cosine")

        matching_status = recommendSystem.matching()

        print(matching_status)

        for idx, matching_data in enumerate(matching_status):
            user1, user2 = set(matching_data)
            instance = User.query.filter_by(schoolNumber=user1).first_or_404(
                description='There is no user with {}. Please Login First.'.format(user1))
            setattr(instance, "matched", True)
            setattr(instance, "matchedUser", user2)
            commit_changes()

            instance = User.query.filter_by(schoolNumber=user2).first_or_404(
                description='There is no user with {}. Please Login First.'.format(user2))
            setattr(instance, "matched", True)
            setattr(instance, "matchedUser", user1)
            commit_changes()

        return make_response(jsonify({"status": "success", "message": "Matching Successfully!"}), 200)

    return make_response(jsonify({"status": "fail", "message": "Please Request with Appropriate Method"}))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port="4000", debug=True)
