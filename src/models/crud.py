from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #criando o modelo para inserir no banco de dados

class Inserttable(db.Model):
    __tablename__ = 'inserttable'
    id = db.column(db.Integer, primary_key=True, autoincrement=True)
    