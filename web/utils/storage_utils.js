const setAuthKey = (key) => {
    localStorage.setItem("auth", key);
};

const getAuthKey = () => {
    return localStorage.getItem("auth");
};

const getQuestionAnswers = () => {
    let answers = localStorage.getItem("answers");

    if (answers) {
        answers = JSON.parse(answers);
    } else {
        answers = [undefined, undefined, undefined, undefined, undefined, undefined];
    }

    return answers;
};

const setQuestionAnswers = (questionIdx, answerIdx) => {
    let answers = getQuestionAnswers();

    answers[questionIdx] = answerIdx;

    localStorage.setItem("answers", JSON.stringify(answers));
};

export { setAuthKey, getAuthKey, getQuestionAnswers, setQuestionAnswers };
