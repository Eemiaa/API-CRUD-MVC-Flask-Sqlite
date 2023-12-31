from flask import Blueprint
import controllers.crudController as contr

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/create', methods=['POST'])(contr.create)
blueprint.route('/read', methods=['GET'])(contr.read)
blueprint.route('/update', methods=['POST'])(contr.update)
blueprint.route('/delete', methods=['DELETE'])(contr.delete)

