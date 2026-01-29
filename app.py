import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>App Runner Demo</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f4; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
            h1 { color: #333; }
            p { color: #666; }
            .badge { background-color: #e6f7ff; color: #0070f3; padding: 5px 10px; border-radius: 15px; font-size: 0.9em; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Ciao! 👋</h1>
            <p>La tua webapp è attiva su <strong>AWS App Runner</strong>.</p>
            <p class="badge">Runtime: Python 3.11</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # App Runner imposta la variabile d'ambiente PORT, di default 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
