from exts import db

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), unique=True, nullable=False)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    cor = db.Column(db.String(30))
    renavam = db.Column(db.String(20))
    chassi = db.Column(db.String(50))
    combustivel = db.Column(db.String(20))
    km = db.Column(db.Float)
    situacao = db.Column(db.String(30))
    data_aquisicao = db.Column(db.String(20))
    observacoes = db.Column(db.Text)
