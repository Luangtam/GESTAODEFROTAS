from flask import Blueprint, render_template
from flask_login import login_required

# Cria o Blueprint de Configurações
configuracoes_bp = Blueprint('configuracoes_bp', __name__, url_prefix='/configuracoes')

@configuracoes_bp.route('/')
@login_required
def configuracoes():
    return render_template('configuracoes.html')
