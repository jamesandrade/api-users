import bcrypt

from src.server.database.Database import User

class AddUserService():
    def execute(self, data):
        passHash = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())

        newUser = User(
            name=data["name"],
            email=data["email"],
            password= passHash,
            avatar=data["avatar"]
        )
        try:
            newUser.save()
        except:
            return "Error"
        
        return data

addUserService = AddUserService()
