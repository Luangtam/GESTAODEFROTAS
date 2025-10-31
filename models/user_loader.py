

# models/user.py (exemplo)
class User:
    def __init__(self, id, username, senha):
        self.id = id
        self.username = username
        self.senha = senha

    # Flask-Login exige essas propriedades
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
