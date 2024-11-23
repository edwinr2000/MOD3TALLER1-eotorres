from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = "root"
DB_PASSWORD = "142000"
DB_HOST = "localhost"
DB_NAME = "tablas"

# Configuración de la base de datos
engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()