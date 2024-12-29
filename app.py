from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
from routes.clients_route import clients

app = Flask(__name__)
app.secret_key = "tr4rt34t334yt"

settings = []
with open("settings.json") as file:
    settings = json.load(file)



if __name__ == '__main__':

    app.run(
        debug=True,
        host=settings["flask"]["host"],
        port=settings['flask']['port']
    )