from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        api = Api(app)
        app.config['api'] = api

        from application import routes  # noqa

        return app


"""line 17: #noqa = NO-QA (NO Quality Assurance)"""
"""It's generally used in Python code to ignore PEP8 warnings"""
"""Adding # noqa to a line indicates that the linter (a program that automatically checks code quality) 
should not check this line. Any warnings that code may have generated will be ignored"""
