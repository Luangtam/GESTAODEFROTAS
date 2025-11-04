from flask import Blueprint, render_template, request, redirect, url_for, flash

veiculo_bp = Blueprint('veiculo_bp', __name__, url_prefix='/veiculo')

@veiculo_bp.route('/', methods=['GET', 'POST'])
def veiculo():
    if request.method == 'POST':
        # Captura os dados do formulário
        placa = request.form.get('placa')
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        ano = request.form.get('ano')
        cor = request.form.get('cor')
        renavam = request.form.get('renavam')
        chassi = request.form.get('chassi')
        combustivel = request.form.get('combustivel')
        km = request.form.get('km')
        situacao = request.form.get('situacao')
        data_aquisicao = request.form.get('data_aquisicao')
        observacoes = request.form.get('observacoes')

        # Aqui você pode salvar no banco (ex: SQLAlchemy)
        flash(f'Veículo {placa} cadastrado com sucesso!', 'success')

        # Redireciona para a mesma página após o cadastro
        return redirect(url_for('veiculo_bp.veiculo'))

    # Renderiza a página de cadastro de veículos
    return render_template('veiculo.html')
