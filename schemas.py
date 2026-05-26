from pydantic import BaseModel


class UserCreate(BaseModel):

    username: str
    password: str


class LoginSchema(BaseModel):

    username: str
    password: str


class SearchQuery(BaseModel):

    query: str