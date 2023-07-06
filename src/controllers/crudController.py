from flask import jsonify, make_response
from models.crud import Inserttable
import services.crud_service as srv

def create():
    srv.create()
    return make_response(jsonify(msg = 'ok'))
