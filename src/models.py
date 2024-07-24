import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique= True)
    passw = Column(String(250), nullable=False, unique= True)
    fecha_subscripcion= Column(String(250))

    #favoritos = relationship('Favoritos', back_populates='user')

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id_favorito = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=False)
    id_planetas = Column(Integer, ForeignKey('planetas.id_planeta'), nullable=False)
    id_vehiculos = Column(Integer, ForeignKey('vehiculos.id_vehiculo'), nullable=False)
    id_personajes = Column(Integer, ForeignKey('personajes.id_personaje'), nullable=False)

    #user = relationship('Users', back_populates='favoritos')

class Planetas(Base):
    __tablename__ = 'planetas'
    id_planeta = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False, unique= True)
    diametro = Column(Integer)
    poblacion = Column(Integer)
    clima = Column(String(250))
    #id_user= Column(Integer, ForeignKey('users.id_user'))

class Personajes(Base):
    __tablename__ = 'personajes'
    id_personaje = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False, unique= True)
    genero = Column(String(250))
    altura = Column(Integer)
    peso = Column(Integer)
    #id_user= Column(Integer, ForeignKey('users.id_user'))

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id_vehiculo = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False, unique= True)
    modelo = Column(String(250))
    fabricante = Column(String(250))
    num_pasajeros = Column(Integer)
    costo = Column(Integer)
    #id_user= Column(Integer, ForeignKey('users.id_user'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
