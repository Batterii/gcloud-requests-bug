import logging
from flask import Flask
from testmodel import TestModel

app = Flask(__name__)

@app.route('/')
def index():
    TestModel.get_by_id(1)
    return 'Hello World!'


@app.errorhandler(500)
def server_error(e):
    logging.exception('error!')
    return ('server error: <pre>{}</pre>'.format(e), 500)
