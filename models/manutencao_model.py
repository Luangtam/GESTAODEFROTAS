from exts import db

class Manutencao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veiculo = db.Column(db.String(10))
    tipo = db.Column(db.String(50))
    descricao = db.Column(db.Text)
    data_entrada = db.Column(db.String(20))
    data_saida = db.Column(db.String(20))
    km = db.Column(db.Float)
    custo = db.Column(db.Float)
    oficina = db.Column(db.String(100))
    status = db.Column(db.String(50))
    observacoes = db.Column(db.Text)
