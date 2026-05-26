from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    role = Column(String)


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    company_name = Column(String)
    document_type = Column(String)
    file_path = Column(String)