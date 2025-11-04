from flask import Blueprint, render_template
from flask_login import login_required


relatorio_bp = Blueprint('relatorio_bp', __name__, url_prefix='/relatorio')

@relatorio_bp.route('/')
@login_required
def relatorio():
    return render_template('relatorio.html')
