import Head from "next/head";
import Image from "next/image";

export default function Login() {
    return (
        <main className='w-screen h-screen bg-gray-100'>
            <div className='w-full h-full relative flex flex-col items-center justify-center'>
                <form className='w-full items-center justify-center'>
                    <div className='flex items-center border-b border-teal-500 py-2'>
                        <input
                            className='appearance-none bg-transparent text-3xl font-semibold border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none'
                            type='text'
                            placeholder='학번을 입력해주세요'
                            aria-label='School Number'
                        />
                    </div>
                    {/* <div className='flex items-center border-b border-teal-500 py-2'>
                        <input
                            className='appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none'
                            type='text'
                            placeholder='비밀번호'
                            aria-label='Password'
                        />
                    </div> */}
                    <button
                        className='flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded'
                        type='button'>
                        Sign Up
                    </button>
                </form>
            </div>
        </main>
    );
}
