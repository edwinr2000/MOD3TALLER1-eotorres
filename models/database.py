from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Credenciales de la base de datos
DB_USER = "root"
DB_PASSWORD = "142000"
DB_HOST = "localhost"
DB_NAME = "TABLAS"

# Crear el motor de la base de datos
engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# Crear la base para los modelos
Base = declarative_base()

# Crear el 'sessionmaker' para la sesión de SQLAlchemy
Session = sessionmaker(bind=engine)

# Crear una instancia de la sesión
session = Session()
