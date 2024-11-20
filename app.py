from flask import Flask
from controllers.cuidador_controller import cuidador_bp
from controllers.perro_controller import perro_bp

app = Flask(__name__)

# Registrar controladores
app.register_blueprint(cuidador_bp)
app.register_blueprint(perro_bp)

if __name__ == '__main__':
    app.run(debug=True)