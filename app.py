from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Página inicial - versão em português."""
    return render_template("index.html")


@app.route("/en")
def index_en():
    """Home page - English version."""
    return render_template("index_en.html")


@app.route("/contato")
def contato():
    """Página de contato - versão em português."""
    return render_template("contato.html")


@app.route("/en/contact")
def contact_en():
    """Contact page - English version."""
    return render_template("contact.html")


if __name__ == "__main__":
    # debug=True facilita o desenvolvimento (recarrega o servidor a cada alteração)
    app.run(debug=True, host="0.0.0.0", port=5000)
