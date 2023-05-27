
from flask import Flask
from lib.config import Environment
from lib.db import db
from lib.encoders import CustomJsonProvider

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Environment.db_uri
app.json = CustomJsonProvider(app)
db.init_app(app)
