from flask import Blueprint
from controllers.crudController import create, read, update, delete

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/read', methods=['GET'])(read)
blueprint.route('/update', methods=['GET'])(update)
blueprint.route('/delete', methods=['GET'])(delete)
