from flask import Flask
from routes.blueprint import blueprint
from models import crud
from database.config import engine

def create_app():
    app = Flask(__name__)
    crud.Base.metadata.create_all(bind=engine)
    return app

app = create_app()

app.register_blueprint(blueprint)

if __name__ == '__main__':  # Running the app
    app.run(port=5000, debug=True)