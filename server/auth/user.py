import jwt


def encode_user_to_jwt(schoolNumber, hashed_password, secret):
    logined_user = {
        "schoolNumber": schoolNumber,
        "password": hashed_password
    }

    encoded_jwt_token = jwt.encode(logined_user, secret, algorithm="HS256")

    return encoded_jwt_token


def decode_jwt_to_user(jwt_token, secret):
    data = jwt.decode(jwt_token, secret, algorithms="HS256")

    return data


def get_schoolNumber(jwt_token, secret):
    data = decode_jwt_to_user(jwt_token, secret)

    return data.get('schoolNumber')