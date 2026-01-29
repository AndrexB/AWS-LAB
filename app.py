import os
from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/env")
def env_info():
    # mostra un dettaglio utile sul deploy e la porta in uso
    port = os.environ.get("PORT", "undefined")
    return f"Hello from AWS App Runner! PORT={port}", 200

@app.route("/health")
def health():
    # endpoint semplice per health checks
    return "OK", 200

if __name__ == "__main__":
    # per debug locale
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
