from flask import Flask
from flask_login import LoginManager
from Models.database import session
from Controllers.user_controller import auth_bp

app = Flask(__name__)
app.secret_key = 'clave-secreta-unica'

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

# Registrar blueprints
app.register_blueprint(auth_bp)

@login_manager.user_loader
def load_user(user_id):
    from Models.user import User
    return session.query(User).get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)