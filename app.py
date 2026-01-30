import os
import boto3
from flask import Flask, render_template_string
from prometheus_client import generate_latest, Counter, Histogram, CONTENT_TYPE_LATEST

app = Flask(__name__)

# METRICHE
REQUESTS = Counter('webapp_calls_total', 'Richieste totali', ['endpoint'])
LATENCY = Histogram('webapp_latency_seconds', 'Tempo di risposta')

@app.route('/')
@LATENCY.time()
def home():
    REQUESTS.labels(endpoint='/').inc()
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>body { background: #0f172a; color: white; padding: 50px; }</style>
    </head>
    <body>
        <div class="container card bg-dark p-5 shadow-lg">
            <h1 class="text-info">🚀 Monitoring Dashboard</h1>
            <p class="lead">Stato: <span class="badge bg-success">Online</span></p>
            <hr class="bg-light">
            <p>Le metriche sono esposte su <code>/metrics</code></p>
            <a href="/metrics" class="btn btn-outline-info">Vedi Metriche Raw</a>
        </div>
    </body>
    </html>
    """)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
