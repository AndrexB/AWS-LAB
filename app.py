from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello App Runner 🚀"

if __name__ == "__main__":
    # Port 8000 perché App Runner espone quella porta
    app.run(host="0.0.0.0", port=8000)
