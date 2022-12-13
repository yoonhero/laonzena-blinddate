import { getAuthHeader } from "./auth";
import axios from "axios";
import { setAuthKey } from "./storage_utils";

const API_SERVER_URL = process.env.NEXT_PUBLIC_API_SERVER;

const LoginAPI = async ({ schoolNumber, password }) => {
    const data = {
        schoolNumber: schoolNumber,
        password: password,
    };

    const headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json",
    };

    try {
        const response = await axios.post(API_SERVER_URL + "/login", data, headers);
        const status = response.data.status;
        const message = response.data.message;

        if (status == "success") {
            const authKey = response.data.Authorization;
            setAuthKey(authKey);

            return [true, message];
        } else {
            return [false, message];
        }
    } catch (e) {
        console.log(e);
        return false, "Fail to network with server.";
    }
};

const CreateUserAPI = async ({ schoolNumber, password, phoneNumber }) => {
    const data = {
        schoolNumber: schoolNumber,
        password: password,
        phoneNumber: phoneNumber,
    };

    const headers = {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json",
    };

    try {
        const response = await axios.post(API_SERVER_URL + "/create_user", data, headers);
        const status = response.data.status;
        const message = response.data.message;

        if (status == "success") {
            const authKey = response.data.Authorization;
            setAuthKey(authKey);

            return [true, message];
        } else {
            return [false, message];
        }
    } catch (e) {
        console.log(e);
        return false, "Fail to network with server.";
    }
};

const UpdateUserInfoAPI = async ({ questionIdx, answerIdx }) => {
    const data = {
        answer_idx: answerIdx,
    };

    const headers = getAuthHeader();

    axios.defaults.headers.common["Authorization"] = headers.Authorization;

    let url = API_SERVER_URL + `/question/${questionIdx}`;

    try {
        const response = await axios.post(url, data, headers);
        const status = response.data.status;

        if (status == "success") {
            return true;
        } else {
            return false;
        }
    } catch (e) {
        console.log(e);
    }
};

const getMatchingStatusAPI = async ({}) => {
    const headers = getAuthHeader();

    let url = API_SERVER_URL + `/matching`;

    try {
        const response = await axios.get(url, data, headers);
        const status = response.data.status;

        if (status == "success") {
            return response.data.user;
        } else {
            return false;
        }
    } catch (e) {
        console.log(e);
    }
};

export { LoginAPI, CreateUserAPI, UpdateUserInfoAPI, getMatchingStatusAPI };
