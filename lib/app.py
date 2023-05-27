
from flask import Flask
from lib.config import Environment
from lib.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Environment.db_uri
db.init_app(app)
