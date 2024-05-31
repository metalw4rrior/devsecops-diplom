from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return "Hello, DevSecOps!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
