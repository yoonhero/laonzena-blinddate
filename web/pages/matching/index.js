import Head from "next/head";
import Image from "next/image";
import { useRouter } from "next/router";
import { useState, useEffect, use } from "react";
import { Header } from "../../components/header";
import { getAuthKey } from "../../utils/storage_utils";

export default function Matching() {
    const router = useRouter();
    const [authed, setAuthed] = useState();

    useEffect(() => {
        let auth = getAuthKey() ? true : false;

        setAuthed(auth);
    }, []);

    useEffect(() => {
        if (!authed) {
            router.push("/login");
        }
    }, [authed]);

    return (
        <>
            <Head>
                <title>라온제나 - 매칭 현황</title>
            </Head>
            <main className="w-screen h-screen bg-gray-100 bg-[url('/background.svg')]">
                <Header />
                <div className='w-full h-[80vh] relative flex flex-col items-center justify-center p-2'>
                    <div className='flex flex-col items-center'>
                        <h1 className='text-4xl md:text-6xl font-black '>짝을 찾는중...</h1>
                        <span className='m-4 text-xl'>12/20일 공개 예정이랍니다!</span>

                        <div className='scale-[1.2] magnifying-container'>
                            <div className='magnifying'>
                                <div className='handle'></div>
                                <div className='middle'></div>
                                <div className='top'></div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </>
    );
}
