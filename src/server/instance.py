from flask import Flask
from flask_restx import Api
from flask_cors import CORS

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        CORS(self.app)
    def run(self, ):
        self.app.run(debug=True)
        
server = Server()