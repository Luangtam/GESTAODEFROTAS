# app.py
from flask import Flask
from flask_login import LoginManager
from controllers.login_controller import login_bp
from controllers.dashboard_controller import dashboard_bp
from controllers.veiculo_controller import veiculo_bp
from controllers.manutencao_controller import manutencao_bp
from controllers.perfil_controller import perfil_bp
from controllers.relatorio_controller import relatorio_bp
from controllers.configuracoes_controller import configuracoes_bp
from models.user_loader import User
from flask_sqlalchemy import SQLAlchemy

# Cria a aplicação Flask
app = Flask(__name__)
app.secret_key = 'chave_secreta_segura_aqui_123'

# Configura o gerenciador de login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_bp.login'

# Função obrigatória para Flask-Login
@login_manager.user_loader
def load_user(user_id):
    if user_id == "1":
        return User(id=1, username="admin", senha="123")
    return None

# Registro dos Blueprints
app.register_blueprint(login_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(veiculo_bp)
app.register_blueprint(manutencao_bp)
app.register_blueprint(perfil_bp)
app.register_blueprint(relatorio_bp)
app.register_blueprint(configuracoes_bp)




# Configuração do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/frota_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Roda o servidor
if __name__ == '__main__':
    app.run(debug=True)
