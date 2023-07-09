from flask import jsonify, make_response
import services.crud_service as srv

def create():
    codigo, msg =srv.create()
    return make_response(jsonify(codigo = codigo, mensagem = msg))

def read():
    codigo, msg =srv.read()
    return make_response(jsonify(codigo = codigo, mensagem = msg))

def update():
    codigo, msg =srv.update()
    return make_response(jsonify(codigo = codigo, mensagem = msg))

def delete():
    codigo, msg =srv.delete()
    return make_response(jsonify(codigo = codigo, mensagem = msg))
