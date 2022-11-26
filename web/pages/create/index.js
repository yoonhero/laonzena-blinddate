import Head from "next/head";
import Image from "next/image";
import { useRouter } from "next/router";
import { useState, useEffect } from "react";

import { Header } from "../../components/header";
import { CreateUserAPI } from "../../utils/api";
import { getAuthKey } from "../../utils/storage_utils";

export default function Login() {
    const router = useRouter();

    const [schoolNumber, setSchoolNumber] = useState("");
    const [password, setPassword] = useState("");
    const [onlySema, setOnlySema] = useState("");

    useEffect(() => {
        let auth = getAuthKey() ? true : false;

        if (auth) {
            router.push("/question/1");
        }
    }, []);

    const loginRequest = async () => {
        // CREATE User
        // axios.post(schooNumber, password)
        const oonlySema = process.env.NEXT_PUBLIC_SECRET_KEY;

        // TODO: Modal Alert
        if (onlySema != String(oonlySema)) {
            return;
        }

        if (schoolNumber == "" || password == "") {
            return;
        }

        if (schoolNumber.length != 5) {
            return;
        }

        const status = await CreateUserAPI({ schoolNumber, password });

        if (status) {
            router.push("/question/1");
        } else {
            console.log("error...");
        }

        // setAuthKey(key)
    };

    return (
        <>
            <Head>
                <title>만남의 광장 - 유저생성</title>
            </Head>
            <main className="w-screen h-screen bg-gray-100">
                <Header />
                <div className="w-full h-[80vh] relative flex flex-col items-center justify-center">
                    <form className="flex flex-col items-center justify-center">
                        <div className="m-5 flex items-center " key={1}>
                            <input
                                onChange={(e) =>
                                    setSchoolNumber(e.target.value)
                                }
                                value={schoolNumber}
                                className={`appearance-none bg-transparent text-3xl font-semibold  border-b-2 border-gray-300 transform transition east-in-out duration-300  w-full text-gray-700 mr-3 py-3 px-5 leading-tight focus:outline-none ${
                                    schoolNumber.length != 5
                                        ? "focus:border-red-500"
                                        : "focus:border-green-500 "
                                }`}
                                type="text"
                                placeholder="학번을 입력해주세요"
                                aria-label="School Number"
                            />
                        </div>
                        <div className="m-5 flex items-center" key={2}>
                            <input
                                onChange={(e) => setPassword(e.target.value)}
                                value={password}
                                className="appearance-none bg-transparent text-3xl font-semibold  border-b-2 border-gray-300 transform transition east-in-out duration-300  w-full text-gray-700 mr-3 py-3 px-5 leading-tight focus:border-teal-500 focus:outline-none"
                                type="text"
                                placeholder="비밀번호"
                                aria-label="Password"
                            />
                        </div>
                        <div className="m-3 flex items-center" key={2}>
                            <input
                                onChange={(e) => setOnlySema(e.target.value)}
                                value={onlySema}
                                className={`appearance-none bg-transparent text-md md:text-xl font-semibold  border-b-2 border-gray-300 transform transition east-in-out duration-300  w-full text-gray-700 mr-3 py-4 px-4 md:px-8 leading-tight focus:border-red-500 focus:outline-none text-center`}
                                type="text"
                                placeholder="세마고 학습자료실 비밀번호"
                                aria-label="Security"
                            />
                        </div>
                        <div className="mt-10" key={3}>
                            <button
                                onClick={() => loginRequest()}
                                className="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-2xl font-semibold border-4 text-white py-2 px-6 rounded-2xl"
                                type="button">
                                다음으로
                            </button>
                        </div>
                    </form>
                </div>
            </main>
        </>
    );
}
