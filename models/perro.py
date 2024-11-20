from sqlalchemy import Column, Integer, String, Float
from database import Base

class Perro(Base):
    __tablename__ = 'perros'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    raza = Column(String)
    edad = Column(Integer)
    peso = Column(Float)
    ID_GUARDERIA = Column(Integer)
    ID_CUIDADOR = Column(Integer)