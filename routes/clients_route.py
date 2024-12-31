import os
import sys
from flask import request, Blueprint, Flask, render_template, redirect, session, sessions, url_for, send_file, flash
import mysql.connector
import json
import io
import csv
from models.Client import Client
from extensions import db

clients = Blueprint('clients', __name__)

@clients.route('/')
async def index():
    clients = db.session.query(Client).all()
    return render_template('clients/index.jinja', clients=clients)
