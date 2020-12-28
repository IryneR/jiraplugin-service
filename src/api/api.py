#from flask import Flask
#from flask_restful import Resource, Api, reqparse, abort, marshal, fields

# Initialize Flask
#app = Flask(__name__)
#api = Api(app)


from flask import Flask
app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)