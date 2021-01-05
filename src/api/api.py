import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/hash', methods=['GET'])
def api_hash():
# hash for string
    return jsonify({'hash': hash('thedarkdog.attlasian.net')})

@app.route('/')
def hello_world():
    return 'My app in Docker'

app.run()