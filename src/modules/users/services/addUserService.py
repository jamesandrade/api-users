from src.server.database.Database import User

class AddUserService():
    def execute(self, data):
        newUser = User(
            name=data["name"],
            email=data["email"],
            password=data["password"],
            avatar=data["avatar"]
        )
        try:
            newUser.save()
        except:
            return "Error"
        
        return data

addUserService = AddUserService()
