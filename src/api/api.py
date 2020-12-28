#from flask import Flask
#from flask_restful import Resource, Api, reqparse, abort, marshal, fields

# Initialize Flask
#app = Flask(__name__)
#api = Api(app)


import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run()