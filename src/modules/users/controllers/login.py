from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from src.server.instance import server
app, api = server.app, server.api


@api.route('/login', methods=['POST'])
class login(Resource):
    def post(self, ):
        data = request.json
        return data    
