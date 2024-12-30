from extensions import db
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, declarative_base

class Client(db.Model):
    __tablename__ = 'Clients'

    dni = db.Column(String(50), primary_key=True)
    nombre = db.Column(String(50))
    apellidos = db.Column(String(50))
    direccion = db.Column(String(200))
    email = db.Column(String(200))
    telefono = db.Column(String(200))
    googlemap_link = db.Column(String(400))

    def __init__(self, dni, nombre, apellidos, direccion, email, telefono, googlemap_link):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        self.googlemap_link = googlemap_link
