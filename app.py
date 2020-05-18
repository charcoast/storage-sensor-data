from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.receive_data import ReceiveData
from resources.ping import Ping

app = Flask(__name__)
app.secret_key = 'sadasdada'
api = Api(app)

api.add_resource(ReceiveData, '/send')
api.add_resource(Ping, '/ping')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)