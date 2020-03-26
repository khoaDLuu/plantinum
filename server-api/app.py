import os

from flask import Flask
from flask_migrate import Migrate
from models import db, Plant

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# migrate = Migrate(app, db)

@app.route('/')
def hello():
    return {'app': 'plantinum api'}


if __name__ == '__main__':
    app.run(debug=True)
