from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("NAME", "World")
    return f"Hello, {name}! 🚀"

if __name__ == "__main__":
    # Usa la porta fornita da App Runner
    port = int(os.environ.get("PORT", 8000))
    # Bind a tutte le interfacce
    app.run(host="0.0.0.0", port=port)
