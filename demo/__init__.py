import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config[secret_key]

basedir = os.path.abspath(os.path.dirname(__file__))

app.config=['SQLALCHEMY_DATEBASE_URI'] = 'sqlite://'

app.config[trac_notification]

db = SQLAlchemy(app)

Migrate(app, db)