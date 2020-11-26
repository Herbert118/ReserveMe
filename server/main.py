import os

from flask import Flask

from api.conf.config import SQLALCHEMY_DATABASE_URI
from api.routes import generate_routes
from api.database.database import db
from api.database.db_init import create_admin_user


def create_app():

    app = Flask(__name__)

    app.config['DEBUG'] = True

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    if not os.path.exists(SQLALCHEMY_DATABASE_URI):
        db.app = app
        db.create_all()
    return app


if __name__ == '__main__':

    app = create_app()
    db.create_all()
    create_admin_user()
    generate_routes(app)
    app.run(port=5000, debug=True, host='localhost', use_reloader=True)
