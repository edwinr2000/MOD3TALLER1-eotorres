from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from Models.database import Base

class Perro(Base):
    __tablename__ = 'perros'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    raza = Column(String(50))
    edad = Column(Integer)
    peso = Column(Float)
    id_guarderia = Column(Integer, ForeignKey('guarderias.ID'))
    id_cuidador = Column(Integer, ForeignKey('cuidadores.ID'))
    update = Column(DateTime)
