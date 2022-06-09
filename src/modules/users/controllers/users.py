from flask import Flask, request, jsonify
from flask_restx import Api, Resource

from src.modules.users.services.addUserService import addUserService
from src.modules.users.services.deleteUserService import deleteUserService
from src.server.instance import server
app, api = server.app, server.api


@api.route('/users', methods=['GET','POST', 'PUT', 'DELETE'])
class user(Resource):
    def get(self, ):
        data = request.json
        return data  

    def post(self, ): 
        data = request.json
        x = addUserService.execute(data)
        return x

    def delete(self,):
        data = request.json
        x = deleteUserService.execute(data)
        return x