from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

# Credenciales de la base de datos
DB_USER = "root"     
DB_PASSWORD = "142000" 
DB_HOST = "localhost"   
DB_NAME = "TABLAS"         

engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

Base = declarative_base()

class Cuidador(Base):
    __tablename__ = 'cuidadores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String)
    ID_GUARDERIA = Column(Integer)

class Perro(Base):
    __tablename__ = 'perros'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    raza = Column(String)
    edad = Column(Integer)
    peso = Column(Float)
    ID_GUARDERIA = Column(Integer)
    ID_CUIDADOR = Column(Integer)



class Usuario(UserMixin):
    def __init__(self, id, username, password, es_admin=False):
        self.id = id
        self.username = username
        self.password = password
        self.es_admin = es_admin

# Instancias de usuarios para pruebas
usuarios = [
    Usuario(id=1, username="admin", password="admin123", es_admin=True),
    Usuario(id=2, username="cliente1", password="password1"),
    Usuario(id=3, username="cliente2", password="password2")
]

def obtener_usuario_por_username(username):
    return next((u for u in usuarios if u.username == username), None)

