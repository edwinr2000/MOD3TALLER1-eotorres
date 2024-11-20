from flask import Blueprint
from models.database import session
from models.cuidador import Cuidador
from models.perro import Perro

cuidador_bp = Blueprint("cuidador", __name__)

@cuidador_bp.route('/mario')
def assign_mario():
    mario = session.query(Cuidador).filter(Cuidador.nombre == 'Mario López Gutierrez').first()
    if mario:
        session.query(Perro).filter(Perro.peso < 3).update({"ID_CUIDADOR": mario.id})
        session.commit()
        return "Los perros de menos de 3 kg han sido asignados a Mario."
    else:
        return "No se encontró a Mario."
