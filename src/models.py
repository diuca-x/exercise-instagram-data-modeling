import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable =False)
    dni = Column(Integer)
    nac = Column(Integer)
    tel = Column(Integer)
    email = Column(String(100),nullable = False)
    password = Column(String(100), nullable = False)
    identificador = Column(String(100), nullable= False)

class Comentarios (Base):
    __tablename__ = "comentarios"
    id = Column(Integer, primary_key=True)
    text = Column(String(1000), nullable = False)
    user_id = Column(Integer, ForeignKey("User.id"))
    publi_id = Column(Integer, ForeignKey("Publicaciones.id"))

class Publicaciones(Base):
    __tablename__ = "publicaciones"
    id = Column(Integer, primary_key=True)
    src = Column(String(1000), nullable = False)
    descripcion = Column(String(420))
    user_id = Column(Integer, ForeignKey("User.id"))

class Historias (Base):
    __tablename__ = "historias"
    id = Column(Integer, primary_key=True)
    src = Column(String(1000), nullable = False) 
    user_id = Column(Integer, ForeignKey("User.id"))

class Notificaciones(Base):
    __tablename__ = "notificaciones"
    id = Column(Integer, primary_key=True)
    id_origen = Column(Integer, nullable=False)
    id_destino = Column(Integer, nullable=False)
    tipo = Column(String,nullable = False) #si es por una etiquetacion, seguidor, like etc

class Follower(Base): 
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    te_sigue = Column(Boolean, nullable = False)
    lo_sigues = Column(Boolean, nullable = False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
