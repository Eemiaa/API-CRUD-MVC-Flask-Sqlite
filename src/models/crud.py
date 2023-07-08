from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from database.config import Base

class Inserttable(Base):
    __tablename__ = 'inserttable'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    date = Column(Date)
    email = Column(String)
    telefone = Column(String)