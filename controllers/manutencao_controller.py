# controllers/manutencao_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

# Cria o blueprint de Manutenção
manutencao_bp = Blueprint('manutencao_bp', __name__, url_prefix='/manutencao')

@manutencao_bp.route('/', methods=['GET', 'POST'])
def manutencao():
    if request.method == 'POST':
        veiculo = request.form.get('veiculo')
        tipo = request.form.get('tipo')
        descricao = request.form.get('descricao')
        data_entrada = request.form.get('data_entrada')
        data_saida = request.form.get('data_saida')
        km = request.form.get('km')
        custo = request.form.get('custo')
        oficina = request.form.get('oficina')
        status = request.form.get('status')
        observacoes = request.form.get('observacoes')

        # Aqui você pode salvar os dados no banco
        flash(f'Manutenção do veículo {veiculo} registrada com sucesso!', 'success')
        return redirect(url_for('manutencao_bp.manutencao'))

    return render_template('manutencao.html')
