import json
from models import crud
from config import engine

def create():
    try:
        crud.Base.metadata.create_all(bind=engine)
        return '==================TABLES CREATED=================='
    except Exception as e:
        print(e)
        return '==================TABLES NOT CREATED!!!=================='
        