const setAuthKey = (key) => {
    localStorage.setItem("auth", key);
};

const getAuthKey = () => {
    localStorage.getItem("auth");
};

export { setAuthKey, getAuthKey };
