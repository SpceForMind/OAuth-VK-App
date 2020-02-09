import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = "OAuth-VK-App-Secret"

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or 'sqlite:////' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    OAUTH_CREDENTIAL = {
        'id': '7311749',
        'secret': 'XQA6fbn0U7Vw1sFOIV7S'
    }