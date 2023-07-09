import json
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database.config import Base

class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    nascimento = Column(Date)
    email = Column(String)
    telefone = Column(String)
