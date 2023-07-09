import datetime
from flask import jsonify, make_response, request
import services.crud_service as srv

def create():
    entrada = request.get_json()
    codigo, msg = srv.create(nome=entrada['nome'], 
                             nascimento=datetime.date.today(), 
                             email=entrada['email'], 
                             telefone=entrada['telefone'])
    return make_response(jsonify(codigo = codigo, mensagem = msg))

def read():
    entrada = request.get_json()

    codigo, msg =srv.read(id = entrada['id'])
    return make_response(jsonify(codigo = codigo, mensagem = msg))

def update():
    entrada = request.get_json()

    codigo, msg =srv.update(id = entrada['id'],
                            nome=entrada['nome'])
    return make_response(jsonify(codigo = codigo, mensagem = msg))

def delete():
    entrada = request.get_json()

    codigo, msg =srv.delete(id = entrada['id'])
    return make_response(jsonify(codigo = codigo, mensagem = msg))
