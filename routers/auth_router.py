from fastapi import APIRouter

from schemas import UserCreate, LoginSchema
from auth import hash_password, create_token

router = APIRouter(prefix="/auth")

users = []


@router.post("/register")
def register(user: UserCreate):

    new_user = {
        "username": user.username,
        "password": hash_password(user.password)
    }

    users.append(new_user)

    return {
        "message": "User Registered"
    }


@router.post("/login")
def login(user: LoginSchema):

    token = create_token({
        "sub": user.username
    })

    return {
        "access_token": token
    }