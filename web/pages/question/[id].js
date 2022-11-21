import Head from "next/head";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";

export default function Question(id) {
    const router = useRouter();
    const [questionIdx, setQuestionIdx] = useState();
    const [questionType, setQuestionType] = useState("");
    const [question, setQuestion] = useState([]);
    const [answers, setAnswers] = useState([]);
    const [answerIdx, setAnswerIdx] = useState();

    useEffect(() => {
        if (router.query.id) {
            const questionIndex = router.query.id;
            setQuestionIdx(questionIndex);
            // const t_question = axios.get(`http://localhost:4000/question/${questionIdx}`, header={'Content-Type': 'application/json', 'Authorization': #TODO: Key})
            const q = { question: "남자인가요? 여자인가요?", answers: ["남자", "여자"], type: "gender" };
            setQuestionType(q.type);
            setQuestion(q.question);
            setAnswers(q.answers);
        }
    }, [router]);

    useEffect(() => {
        console.log(question);
    }, [question]);

    const clickButton = (idx) => {
        setAnswerIdx(idx);
    };

    return (
        <>
            <Head>
                <title>질문에 답해주세요!</title>
            </Head>
            <main className='w-screen h-screen bg-gray-200'>
                <header className='w-full flex flex-row align-center items-center justify-between h-20 text-black font-bold text-2xl'>
                    <div className='p-4'>LOGO</div>
                    <div className='p-4'>Exit</div>
                </header>

                {/* Question Container */}
                <div className='w-full relative flex flex-col items-center justify-center'>
                    <div className='mt-20 px-6 py-2  rounded-3xl border-[1px] border-black font-md text-xl'>{"하나"}</div>
                    <div className='mt-10'>
                        <span className='text-black font-bold text-5xl'>{question}</span>
                    </div>

                    <div className='mt-10 flex flex-col items-center'>
                        {answers.map((answer, i) => (
                            <div className='m-4'>
                                <button
                                    onClick={() => clickButton(i)}
                                    className={`px-40 py-10 bg-gray-300 border-0 rounded-full hover:bg-gray-800 hover:text-white text-3xl font-xl ${
                                        i == answerIdx && "bg-gray-600 text-white"
                                    }`}>
                                    {answer}
                                </button>
                            </div>
                        ))}
                    </div>
                    <div className='fixed h-20 w-screen bottom-0 flex flex-row items-center justify-around'>
                        <div>
                            <span className='text-2xl'>{`${questionIdx != undefined ? questionIdx : 0}/10`}</span>
                        </div>
                        <div>
                            <button className='px-5 py-3 bg-gray-500 border-0 rounded-full hover:bg-gray-600 text-white text-xl font-xl'>다음</button>
                        </div>
                    </div>
                </div>
            </main>
        </>
    );
}
