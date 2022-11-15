from flask import (
    Flask, render_template, request, jsonify
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import hashlib


from models.index import User
from question import Question
from conn.db_utils import add_instance, delete_instance, get_all
from conn.index import create_app


app = create_app()
question = Question()


@app.route("/question/{id}", methods=["GET", "POST"])
def question_api(id):
    if request.method == "GET":
        # RETURN QUESTION
        target_question = question[id]

        return jsonify(target_question)

    # POST TYPE
    # QUESTION NUMBER 1~
    # ANSWER INDEX 1~
    elif request.method == "POST":
        # SAVE THE DICTIONARY
        try:
            params = request.get_json()

            answer_idx = int(params.get("answer"))
            answer = question.get(id, answer_idx)

            print(answer)

            # TODO: Save the answer to DB
            return jsonify({"status": "success", "message": "Save your answer to the server successfully"})
        except:
            return jsonify({"status": "fail", "message": "Error when process the answer data."})


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

    return jsonify({"status": "success", "message": "Create user successfully"})


@app.route("/login", methods=["POST"])
def login():
    params = request.get_json()

    schoolNumber = params.get('schoolNumber')
    password = params.get('password')

    # hashed_user_password = bcrypt.hashpw(password, salt)
    hashed_user_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    # GET Hashed password from Database using Username
    target_user = User.query.filter(User.schoolNumber == schoolNumber)[0]
    database_password = target_user.password

    if hashed_user_password == database_password:
        # Login
        return jsonify({"status": "success", "message": "login successfully"})

    else:
        return jsonify({"status": "fail", "message": "fail to login"})


@app.route("/users", methods=["GET"])
def user_list():
    users = get_all(User)
    all_users = []
    for user in users:
        new_user = {
            "id": user.id,
            "password": user.password
        }

        all_users.append(new_user)

    return jsonify(all_users), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port="4000", debug=True)
