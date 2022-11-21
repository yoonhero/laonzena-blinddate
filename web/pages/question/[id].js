import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";

export default function Question(id) {
    const router = useRouter();
    const [questionIdx, setQuestionIdx] = useState("");
    const [questionType, setQuestionType] = useState("");
    const [question, setQuestion] = useState([]);
    const [answers, setAnswers] = useState([]);
    const [answerIdx, setAnswerIdx] = useState();

    useEffect(() => {
        if (router.query.id) {
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
            { question: "남자인가요? 여자인가요?", answers: ["남자", "여자"], type: "gender" },
            { question: "몇살인가요?", answers: ["17살", "18살"], type: "age" },
            {
                question: "MBTI가 뭔가요?",
                answers: ["INFP", "ENFP", "ESFJ", "ISFJ", "ISFP", "ESFP", "INTP", "INFJ", "ENFJ", "ENTP", "ESTJ", "ISTJ", "INTJ", "ISTP", "ESTP", "ENTJ"],
                type: "mbti",
            },

            { question: "혈액형이 무엇인가요?", answers: ["A", "B", "AB", "O"], type: "bloodtype" },
            { question: "좋아하는 음식 종류가 무엇인가요?", answers: ["한식", "양식", "중식", "일식"], type: "favoriteFood" },
            { question: "좋아하는 색깔이 무엇인가요?", answers: ["빨강", "주황", "노랑", "초록", "파랑", "보라", "흰색", "검은색"], type: "favoriteColor" },
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

    return (
        <>
            <Head>
                <title>질문에 답해주세요!</title>
            </Head>
            <main className='w-screen h-screen bg-gray-100'>
                <header className='w-full flex flex-row align-center items-center justify-between h-20 text-black font-bold text-2xl'>
                    <div className='p-4'>LOGO</div>
                    <div className='p-4'>Exit</div>
                </header>

                {/* Question Container */}
                <div className='w-full relative flex flex-col items-center justify-center'>
                    <div className='mt-10 px-6 py-2  rounded-3xl border-[1px] border-black font-md text-xl'>
                        {["하나", "둘", "셋", "넷", "다섯", "여섯", "일곱"][questionIdx]}
                    </div>
                    <div className='mt-10 text-center'>
                        <span className='text-black font-semibold text-5xl break-all'>{question}</span>
                    </div>

                    <div className='mt-10 flex flex-col items-center'>
                        {answers.map((answer, i) => {
                            if (questionType == "gender" || questionType == "age") {
                                return (
                                    <>
                                        <div key={i} className='m-4'>
                                            <button
                                                onClick={() => clickButton(i)}
                                                className={`px-20 py-8 md:px-40 md:py-8 bg-gray-200 border-0 rounded-full md:hover:bg-gray-800 md:hover:text-white  text-3xl font-xl ${
                                                    i == answerIdx && "bg-gray-600 text-white"
                                                }`}>
                                                {answer}
                                            </button>
                                        </div>
                                    </>
                                );
                            } else if (questionType == "mbti") {
                                return (
                                    <>
                                        <div key={i} className='m-4'>
                                            <button
                                                onClick={() => clickButton(i)}
                                                className={`px-5 py-2  bg-gray-200 border-0 rounded-full md:hover:bg-gray-800 md:hover:text-white  text-3xl font-xl ${
                                                    i == answerIdx && "bg-gray-600 text-white"
                                                }`}>
                                                {answer}
                                            </button>
                                        </div>
                                    </>
                                );
                            }
                        })}
                    </div>
                    <div className='fixed h-20 w-screen bottom-0 flex flex-row items-center justify-around'>
                        <div>
                            <span className='font-bold text-2xl'>{`${questionIdx != undefined ? questionIdx + 1 : 0}/10`}</span>
                        </div>
                        <div>
                            <button className='px-5 py-3 bg-gray-500 border-0 rounded-full font-bold hover:bg-gray-600 text-white text-xl font-xl'>다음</button>
                        </div>
                    </div>
                </div>
            </main>
        </>
    );
}
