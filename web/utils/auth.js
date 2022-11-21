import { getAuthKey } from "./storage_utils";

const getHeader = () => {
    const authKey = getAuthKey();

    const headers = {
        Authorization: authKey,
    };
    return headers;
};

// TODO: Login Axios Request
const login = () => {};

export { getHeader, login };
