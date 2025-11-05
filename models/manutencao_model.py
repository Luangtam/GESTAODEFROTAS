from exts import db

class Manutencao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veiculo = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_entrada = db.Column(db.Date, nullable=False)
    data_saida = db.Column(db.Date)
    km = db.Column(db.Integer)
    custo = db.Column(db.Float)
    oficina = db.Column(db.String(100))
    status = db.Column(db.String(50))
    observacoes = db.Column(db.Text)
