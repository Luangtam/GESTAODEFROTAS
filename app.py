from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# 🔹 Página de login
@app.route('/')
def login():
    return render_template('login.html')

# 🔹 Dashboard principal
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# 🔹 Páginas do menu lateral
@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/veiculo')
def veiculo():
    return render_template('veiculo.html')

@app.route('/manutencao')
def manutencao():
    return render_template('manutencao.html')

@app.route('/relatorio')
def relatorio():
    return render_template('relatorio.html')

@app.route('/configuracoes')
def configuracoes():
    return render_template('configuracoes.html')

if __name__ == '__main__':
    app.run(debug=True)
