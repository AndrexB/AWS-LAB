from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "L'app funziona!"

if __name__ == '__main__':
    # Questo serve solo se lanci il file localmente
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
