from flask import *
from flask_sqlalchemy import SQLAlchemy
import json
from extensions import db
from routes.clients_route import clients

settings = {}
with open('settings.json') as data:
    settings = json.load(data)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:ikero9090@192.168.1.99/CLIENTES"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(clients)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(
        debug=True,
        host=settings["flask"]["host"],
        port=settings["flask"]["port"]
    )