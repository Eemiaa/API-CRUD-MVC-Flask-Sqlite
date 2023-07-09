import datetime
from models import crud
from database.config import engine, SessionLocal
from models.baseFunctions import BaseFunctions as bf
from sqlalchemy import update as up

db = SessionLocal()

def create(nome, nascimento, email, telefone):
    try:
        db_record = crud.Conta(
                    nome = nome,
                    nascimento = nascimento,
                    email = email,
                    telefone = telefone,
                )
        print(db_record)
        db.add(db_record)
        db.commit()
        return 'Sucess', 'Conta criada com sucesso.'
    except Exception as e:
        print(e)
        return 'Error', 'Não foi possível criar conta.'

def read(id):
    try:
        db_record = db.query(crud.Conta).filter(crud.Conta.id == id).first()

        return 'Sucess', bf.to_json(db_record)
    
    except Exception as e:
        print(e)

        return 'Error', 'Não foi possível obter conta.'

def update(id, nome):
    try:
        db_record = db.query(crud.Conta).filter(crud.Conta.id == id).first()
        db_record.nome = nome

        db.commit()
        return 'Sucess', 'Nome atualizado com sucesso.'
    
    except Exception as e:
        print(e)
        return 'Error', 'Não foi possível fazer o update.'

def delete(id):
    try:
        db_record = db.query(crud.Conta).filter(crud.Conta.id == id).first()
        db.delete(db_record)
        db.commit()
        return 'Sucess', 'Conta deletada com sucesso.'
    except Exception as e:
        print(e)
        return 'Error', 'Não foi possível deletar conta.'
    
