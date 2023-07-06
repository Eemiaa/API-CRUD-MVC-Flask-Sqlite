from flask import Blueprint
import controllers.crudController as contr

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/create', methods=['POST'])(contr.create)
#blueprint.route('/read', methods=['GET'])(contr.read)
#blueprint.route('/update', methods=['GET'])(contr.update)
#blueprint.route('/delete', methods=['GET'])(contr.delete)
