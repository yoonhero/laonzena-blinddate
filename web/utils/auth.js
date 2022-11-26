import { getAuthKey } from "./storage_utils";

const getAuthHeader = () => {
    const authKey = getAuthKey();

    const headers = {
        Authorization: authKey,
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json",
    };
    return headers;
};

export { getAuthHeader };
