import { getAuthHeader } from "./auth";
import axios from "axios";
import { setAuthKey } from "./storage_utils";

const API_SERVER_URL = process.env.NEXT_PUBLIC_API_SERVER;

const LoginAPI = async ({ schoolNumber, password }) => {
  const data = {
    schoolNumber: schoolNumber,
    password: password,
  };

  const header = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json",
  };

  try {
    const response = await axios.post(API_SERVER_URL + "/login", data, header);
    const status = response.data.status;

    if (status == "success") {
      const authKey = response.data.Authorization;
      setAuthKey(authKey);

      return true;
    } else {
      return false;
    }
  } catch (e) {
    console.log(e);
  }
};

const CreateUserAPI = async ({ schoolNumber, password }) => {
  const data = {
    schoolNumber: schoolNumber,
    password: password,
  };

  const header = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json",
  };

  try {
    const response = await axios.post(
      API_SERVER_URL + "/create_user",
      data,
      header
    );
    const status = response.data.status;

    if (status == "success") {
      const authKey = response.data.Authorization;
      setAuthKey(authKey);

      return true;
    } else {
      return false;
    }
  } catch (e) {
    console.log(e);
  }
};

const UpdateUserInfoAPI = async ({ questionIdx, answerIdx }) => {
  const data = {
    answer_idx: answerIdx,
  };

  const header = getAuthHeader();

  let url = API_SERVER_URL + `/question/${questionIdx}`;

  try {
    const response = await axios.post(url, data, header);
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
  const header = getAuthHeader();

  let url = API_SERVER_URL + `/matching`;

  try {
    const response = await axios.get(url, data, header);
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
