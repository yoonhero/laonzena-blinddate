import Head from "next/head";
import Image from "next/image";
import { useRouter } from "next/router";
import { useState, useEffect } from "react";
import { CopyRight } from "../components/copyright";
import { Header } from "../components/header";
import { getAuthKey } from "../utils/storage_utils";

export default function Home() {
    const router = useRouter();
    const [authed, setAuthed] = useState(false);

    useEffect(() => {
        let auth = getAuthKey() ? true : false;

        if (auth) {
            setAuthed(true);
        }
    }, []);
    return (
        <>
            <Head>
                <title>라온제나 - 만남의 광장</title>
            </Head>
            <main className="w-screen h-screen bg-gray-100 bg-[url('/background.svg')]">
                <Header />
                <div className="w-full h-[80vh] relative flex flex-col items-center justify-center p-2">
                    <div className="flex flex-col items-center">
                        <h1 className="text-7xl md:text-9xl font-black ">
                            만남의 광장
                        </h1>
                        <h3 className="text-3xl md:text-6xl font-md m-5">
                            1-2 라온제나
                        </h3>
                    </div>

                    <div className="mt-10 w-[80vw] md:w-[50vw] max-w-sm flex flex-col items-center justify-center p-4 gap-1">
                        <button
                            onClick={() => router.push("/create")}
                            className="w-full text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl focus:outline-none  font-medium rounded-full text-2xl px-10 py-5 text-center mr-2 mb-2">
                            {!authed ? "설문 답하기" : "답변 수정하기"}
                        </button>
                        <button
                            onClick={() => router.push("/matching")}
                            className="break-all w-full text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl  focus:outline-none  font-medium rounded-full text-2xl px-10 py-5 text-center mr-2 mb-2">
                            매칭 현황 보러가기
                        </button>
                    </div>
                    <h3 className="text-xl font-md m-5">
                        운명의 상대를 만날 수 있을까? 바로 알아보자.
                    </h3>
                    <CopyRight />
                </div>
            </main>
        </>
    );
}
