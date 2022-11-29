const Notification = ({ notification }) => {
    return (
        <div className='m-3 '>
            <span className='break-all text-red-400 font-md text-md'>{notification && notification}</span>
        </div>
    );
};

export { Notification };
