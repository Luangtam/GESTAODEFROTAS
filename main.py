from flask import Flask, render_template, request, redirect, url_for, session
from exts import db
from models.veiculo_model import Veiculo

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'

# 🔧 Configuração para conectar ao MySQL (XAMPP)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/gestaofrotas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ========================
# ROTA LOGIN (opcional)
# ========================
@app.route('/', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        if usuario == 'admin' and senha == '123':
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:
            erro = 'Usuário ou senha incorretos.'
    return render_template('login.html', erro=erro)

# ========================
# DASHBOARD
# ========================
@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# ========================
# CADASTRAR VEÍCULO
# ========================
@app.route('/veiculo', methods=['GET', 'POST'])
def veiculo():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        novo = Veiculo(
            placa=request.form['placa'],
            marca=request.form['marca'],
            modelo=request.form['modelo'],
            ano=request.form['ano'],
            cor=request.form['cor'],
            renavam=request.form['renavam'],
            chassi=request.form['chassi'],
            combustivel=request.form['combustivel'],
            km=request.form['km'],
            situacao=request.form['situacao'],
            data_aquisicao=request.form['data_aquisicao'],
            observacoes=request.form['observacoes']
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('listar_veiculos'))  # redireciona para a listagem

    return render_template('cadastro_veiculos/veiculo.html')

# ========================
# LISTAR VEÍCULOS
# ========================
@app.route('/veiculos')
def listar_veiculos():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    veiculos = Veiculo.query.all()
    return render_template('cadastro_veiculos/veiculos.html', veiculos=veiculos)


# ========================
# EDITAR VEÍCULO
# ========================
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)

    if request.method == 'POST':
        veiculo.placa = request.form['placa']
        veiculo.marca = request.form['marca']
        veiculo.modelo = request.form['modelo']
        veiculo.ano = request.form['ano']
        veiculo.km = request.form['km']
        veiculo.situacao = request.form['situacao']

        db.session.commit()
        return redirect(url_for('listar_veiculos'))

    return render_template('cadastro_veiculos/editar_veiculo.html', veiculo=veiculo)


# ========================
# EXCLUIR VEÍCULO
# ========================
@app.route('/excluir/<int:id>')
def excluir_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    return redirect(url_for('listar_veiculos'))



# ========================
# LOGOUT
# ========================
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ========================
# EXECUÇÃO
# ========================
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
