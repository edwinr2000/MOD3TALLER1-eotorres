from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from Models.database import session
from Models.user import User
from Models.perro import Perro 
auth_bp = Blueprint('auth', __name__, template_folder='../Templates')

@auth_bp.route('/')
def home():
    return render_template('base.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = session.query(User).filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            if user.es_admin:
                return redirect(url_for('auth.admin_dashboard'))
            return redirect(url_for('auth.user_dashboard'))
        flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/dashboard/admin')
@login_required
def admin_dashboard():
    if not current_user.es_admin:
        flash("No tienes permisos para acceder aquí", "danger")
        return redirect(url_for('auth.user_dashboard'))
    
    # Consultar todos los perros
    perros = session.query(Perro).all()
    
    return render_template('admin_dashboard.html', perros=perros)

@auth_bp.route('/dashboard/user')
@login_required
def user_dashboard():
    return render_template('user_dashboard.html')
