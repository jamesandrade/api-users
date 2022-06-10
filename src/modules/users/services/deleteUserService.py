import bcrypt

from src.server.database.Database import User

class DeleteUserService():
    def execute(self, data):
        user = User.get(User.email == data["email"])
        password = User.get(User.email == data["email"]).password
        
        if(bcrypt.checkpw(data["password"].encode("utf-8"), password.encode("utf-8"))):
            expect = user.delete_instance()
            if(expect == 1):
                return "Ok"
            else:
                return "Error"          

        return "Error"

deleteUserService = DeleteUserService()
