from flask import Blueprint, render_template, request, redirect, url_for, flash

login_bp = Blueprint('login_bp', __name__)

# Rota de login
@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        
        if usuario == "admin" and senha == "123":
            return redirect(url_for('dashboard_bp.dashboard'))
        else:
            flash("Usuário ou senha inválidos", "danger")

    return render_template('login.html')
