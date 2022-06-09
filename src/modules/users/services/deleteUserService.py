from src.server.database.Database import User

class DeleteUserService():
    def execute(self, data):
        user = User.get(User.email == data["email"])
        password = User.get(User.email == data["email"]).password
        if(password != data["password"]):
            return "Error Password Incorrect"

        expect = user.delete_instance()
        if(expect == 1):
            return "Ok"
        else:
            return "Error"

deleteUserService = DeleteUserService()
