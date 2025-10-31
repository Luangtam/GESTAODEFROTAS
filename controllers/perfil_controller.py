from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Cria o Blueprint de Perfil
perfil_bp = Blueprint('perfil_bp', __name__, url_prefix='/perfil')

@perfil_bp.route('/')
@login_required
def perfil():
    return render_template('perfil.html', user=current_user)
