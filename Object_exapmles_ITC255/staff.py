#  User is object
from user import User

# inheritence
class Staff(User):
    def __init__(self, name, email, securityLevel, position):
        self.name = name
        self.email = email
        self.securityLevel = securityLevel
        self.position = position

    def getPosition(self):
        return self.position

    def __str__(self):
        return super(Staff, self).__str__() +  ","  +self.position

class staff(user):
    def __init__(self, name, email, securitylevel, position);
        self