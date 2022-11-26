import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { Header } from "../../components/header";
import { UpdateUserInfoAPI } from "../../utils/api";
import {
    getQuestionAnswers,
    setQuestionAnswers,
} from "../../utils/storage_utils";

export default function Question() {
    const router = useRouter();
    const [questionIdx, setQuestionIdx] = useState("");
    const [questionType, setQuestionType] = useState("");
    const [question, setQuestion] = useState([]);
    const [answers, setAnswers] = useState([]);
    const [answerIdx, setAnswerIdx] = useState(undefined);

    useEffect(() => {
        try {
            const answersIdxOnStorage = getQuestionAnswers();

            if (!answersIdxOnStorage) {
                setAnswerIdx(undefined);
                return;
            }

            setAnswerIdx(answersIdxOnStorage[questionIdx]);
        } catch (e) {
            setAnswerIdx(undefined);
        }
    }, [questionIdx]);

    useEffect(() => {
        if (router.query.id) {
            if (router.query.id >= 7) {
                return router.push("/");
            }

            const questionIndex = router.query.id - 1;
            setQuestionIdx(questionIndex);
            // const t_question = axios.get(`http://localhost:4000/question/${questionIdx}`, header={'Content-Type': 'application/json', 'Authorization': #TODO: Key})
        }
    }, [router]);

    useEffect(() => {
        if (questionIdx === "") {
            return;
        }
        const qs = [
            {
                question: "남자인가요? 여자인가요?",
                answers: ["남자", "여자"],
                type: "gender",
            },
            { question: "몇살인가요?", answers: ["17살", "18살"], type: "age" },
            {
                question: "MBTI가 뭔가요?",
                answers: [
                    "INFP",
                    "ENFP",
                    "ESFJ",
                    "ISFJ",
                    "ISFP",
                    "ESFP",
                    "INTP",
                    "INFJ",
                    "ENFJ",
                    "ENTP",
                    "ESTJ",
                    "ISTJ",
                    "INTJ",
                    "ISTP",
                    "ESTP",
                    "ENTJ",
                ],
                type: "mbti",
            },

            {
                question: "혈액형이 무엇인가요?",
                answers: ["A", "B", "AB", "O"],
                type: "bloodtype",
            },
            {
                question: "좋아하는 음식 종류가 무엇인가요?",
                answers: ["한식", "양식", "중식", "일식"],
                type: "favoriteFood",
            },
            {
                question: "좋아하는 색깔이 무엇인가요?",
                answers: [
                    "빨강",
                    "주황",
                    "노랑",
                    "초록",
                    "파랑",
                    "보라",
                    "흰색",
                    "검은색",
                ],
                type: "favoriteColor",
            },
        ];
        const q = qs[questionIdx];
        // { question: "남자인가요? 여자인가요?", answers: ["남자", "여자"], type: "gender" };
        setQuestionType(q.type);
        setQuestion(q.question);
        setAnswers(q.answers);
    }, [questionIdx]);

    const clickButton = (idx) => {
        setAnswerIdx(idx);
    };

    const NextPage = () => {
        setQuestionAnswers(questionIdx, answerIdx);

        const status = UpdateUserInfoAPI({ questionIdx, answerIdx });

        if (!status) {
            console.log("error...");
            return;
        }

        setAnswerIdx(undefined);
        if (questionIdx >= 5) {
            return router.push("/matching");
        }
        return router.push(`/question/${questionIdx + 2}`);
    };

    return (
        <>
            <Head>
                <title>질문에 답해주세요!</title>
            </Head>
            <main className="w-screen h-screen bg-gray-100">
                <Header />

                {/* Question Container */}
                <div className="w-full relative flex flex-col items-center justify-center">
                    <div className="mt-3 md:mt-10 px-5 py-2 md:px-6 md:py-2  rounded-3xl border-[1px] border-black font-md text-xl">
                        {
                            ["하나", "둘", "셋", "넷", "다섯", "여섯", "일곱"][
                                questionIdx
                            ]
                        }
                    </div>
                    <div className="mt-4 md:mt-10 text-center">
                        <span className="text-black font-semibold text-3xl sm:text-4xl md:text-5xl break-all">
                            {question}
                        </span>
                    </div>
                    {(questionType == "gender" || questionType == "age") && (
                        <div className="mt-10 flex flex-col items-center">
                            {answers.map((answer, i) => (
                                <div key={i} className="m-2 md:m-4">
                                    <button
                                        onClick={() => clickButton(i)}
                                        className={`px-20 py-5 md:px-40 md:py-8 bg-gray-200 border-0 rounded-full md:hover:bg-gray-800 md:hover:text-white text-2xl sm:text-3xl font-xl ${
                                            i == answerIdx &&
                                            "bg-gray-600 text-white"
                                        }`}>
                                        {answer}
                                    </button>
                                </div>
                            ))}
                        </div>
                    )}
                    {questionType == "mbti" && (
                        <div className="p-2 mt-5 md:mt-10 md:mt-20  h-full overflow-hidden grid grid-cols-3 md:grid-cols-4 grid-flow-row gap-2 items-center">
                            {answers.map((answer, i) => (
                                <div key={i} className="">
                                    <button
                                        onClick={() => clickButton(i)}
                                        className={`px-5 py-2  bg-gray-200 border-0 rounded-full md:hover:bg-gray-800 md:hover:text-white text-xl md:text-3xl font-xl ${
                                            i == answerIdx &&
                                            "bg-gray-600 text-white"
                                        }`}>
                                        {answer}
                                    </button>
                                </div>
                            ))}
                        </div>
                    )}
                    {(questionType == "bloodtype" ||
                        questionType == "favoriteFood") && (
                        <div className="mt-4 md:mt-10 flex flex-col items-center">
                            {answers.map((answer, i) => (
                                <div key={i} className="m-2 md:m-4">
                                    <button
                                        onClick={() => clickButton(i)}
                                        className={`px-20 py-4 md:py-5 md:px-40 md:py-4 bg-gray-200 border-0 rounded-full md:hover:bg-gray-800 md:hover:text-white  text-2xl sm:text-3xl font-xl ${
                                            i == answerIdx &&
                                            "bg-gray-600 text-white"
                                        }`}>
                                        {answer}
                                    </button>
                                </div>
                            ))}
                        </div>
                    )}

                    {questionType == "favoriteColor" && (
                        <div className="mt-4 sm:mt-20 grid grid-cols-3 md:grid-cols-4 grid-flow-row items-center">
                            {/* COLORS  */}
                            {answers.map((answer, i) => (
                                <div key={i} className="m-2">
                                    <button
                                        onClick={() => clickButton(i)}
                                        className={`w-20 h-20 bg-gray-200 border-0 rounded-full transition ease-in-out duration-300 opacity-1 hover:opacity-[0.5] ${
                                            i == answerIdx &&
                                            "ring-offset-0 ring-4"
                                        }`}
                                        style={{
                                            backgroundColor: [
                                                "#DC3535",
                                                "#F49D1A",
                                                "#FFE15D",
                                                "#285430",
                                                "#4D96FF",
                                                "#A149FA",
                                                "#fff",
                                                "#000",
                                            ][i],
                                        }}></button>
                                </div>
                            ))}
                        </div>
                    )}

                    <div className="fixed h-20 w-screen bottom-0 flex flex-row items-center justify-around">
                        <div>
                            <span className="font-bold text-2xl">{`${
                                questionIdx != undefined ? questionIdx + 1 : 0
                            }/6`}</span>
                        </div>
                        <div>
                            <button
                                disabled={answerIdx == undefined}
                                onClick={() => NextPage()}
                                className={`px-5 py-3 bg-gray-500 border-0 rounded-full font-bold hover:bg-gray-600 text-white text-xl font-xl transform transition ${
                                    answerIdx != undefined &&
                                    "bg-green-400 hover:bg-green-500 md:hover:scale-[1.2]"
                                }`}>
                                다음
                            </button>
                        </div>
                    </div>
                </div>
            </main>
        </>
    );
}
