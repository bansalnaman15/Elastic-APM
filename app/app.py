from elasticapm.contrib.flask import ElasticAPM
from flask import Flask

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'FLASKAPP',
    'SECRET_TOKEN': 'BRUH',
    'SERVER_URL': 'http://apm:8200',
    'LOG_LEVEL': 'info'
}
apm = ElasticAPM(app)


@app.route("/")
def index():
    print(1 / 0)
    return "Hello World!"


@app.route('/naman')
def naman():
    return "OYEHELLO"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
