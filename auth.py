from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "secret"


def hash_password(password):

    return password


def verify_password(plain, hashed):

    return plain == hashed


def create_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=2)

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token