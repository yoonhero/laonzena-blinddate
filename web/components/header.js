import Link from "next/link";

const Header = () => {
    return (
        <header className='w-full flex flex-row align-center items-center justify-between h-20 '>
            <div className='p-4 text-black font-semibold md:font-bold text-2xl md:text-3xl'>
                <Link href='/'>LaonZena</Link>
            </div>
            <div className='p-4 text-black font-semibold text-xl '>
                <Link href='http://instagram.com/yoonhero06'>오류문의</Link>
            </div>
        </header>
    );
};

export { Header };
