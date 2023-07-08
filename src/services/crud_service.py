import datetime
from models import crud
from database.config import engine, SessionLocal

db = SessionLocal()

def create():
    try:
        db_record = crud.Conta(
                    nome = "teste",
                    date = datetime.date.today(),
                    email = "teste@gmail.com",
                    telefone = 91984101102,
                )
        print(db_record)
        db.add(db_record)
        db.commit()
        return 'Sucess', 'Conta criada com sucesso.'
    except Exception as e:
        print(e)
        return 'Error', 'Não foi possível criar conta.'

def read():
    try:
        db_record = db.query(crud.Conta).filter(crud.Conta.id == 2).first()
        print(db_record)
        return 'Sucess', 'Conta deletada com sucesso.'
    except Exception as e:
        print(e)
        return 'Error', 'Não foi possível obter conta.'
       
def delete():
    try:
        db_record = db.query(crud.Conta).filter(crud.Conta.id == 1).first()
        db.delete(db_record)
        db.commit()
        return 'Sucess', 'Conta deletada com sucesso.'
    except Exception as e:
        print(e)
        return 'Error', 'Não foi possível deletar conta.'
    
