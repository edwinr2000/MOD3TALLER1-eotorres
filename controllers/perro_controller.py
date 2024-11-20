from flask import Blueprint
from models.database import session
from models.perro import Perro

perro_bp = Blueprint("perro", __name__)

@perro_bp.route('/lassie')
def lassie_count():
    lassie_count = session.query(Perro).filter(Perro.nombre == 'Lassie').count()
    return f"Hay {lassie_count} perros llamados Lassie."