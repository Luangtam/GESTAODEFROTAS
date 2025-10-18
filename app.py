from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# ====== ROTA DE LOGIN ======
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        # Exemplo simples de login fixo (você pode trocar por validação no banco)
        if usuario == "Dudinha" and senha == "123":
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", erro="Usuário ou senha inválidos")
    return render_template("login.html")

# ====== ROTA DO DASHBOARD ======
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ====== EXECUTAR SERVIDOR ======
if __name__ == "__main__":
    app.run(debug=True)
