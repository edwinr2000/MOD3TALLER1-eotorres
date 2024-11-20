from sqlalchemy import Column, Integer, String
from database import Base

class Cuidador(Base):
    __tablename__ = 'cuidadores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String)
    ID_GUARDERIA = Column(Integer)