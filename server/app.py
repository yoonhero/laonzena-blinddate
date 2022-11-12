from flask import (
    Flask, render_template, request, jsonify
)
from flask_cors import CORS
from utils import Question


app = Flask(__name__)

question = Question()


@app.route("/question/{id}", methods=["GET", "POST"])
def question_api(id):
    if request.method == "GET":
        ## RETURN QUESTION
        target_question = question[id]
        
        return jsonify(target_question)
        
    # POST TYPE
    # QUESTION NUMBER 1~
    # ANSWER INDEX 1~
    elif request.method == "POST":
        ## SAVE THE DICTIONARY
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

    username = params.get('username')
    password = params.get('password')
    schoolNumber = params.get('schoolNumber')

    ## TODO: Create USER Row

    return jsonify({"status": "success", "message": "Create user successfully"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port="4000", debug=True)