# Jokes API

## Install
- Install Pip with Python 3.8
- Create venv (`python -m venv ./venv`)
- Activate venv (`source ./venv/bin/activate` with bash/zsh)
- Install the dependencies `pip install -r requirements.txt`
- Copy-paste .env.sample and rename it .env
- Setup a local MySQL DB and update SQLALCHEMY_DATABASE_URI to set the connection string
- Run the migrations from the /db folder
  - TODO: Use alembic instead of MySQL migrations
- Set the flask entry point with `set FLASK_APP=app.py`
  - If to be run in debug mode: `set FLASK_DEBUG=1`
