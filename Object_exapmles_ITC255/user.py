class User():
    def __init__(self,name,email,securityLevel):
        self.name = name
        self.email = email
        self.securityLevel = securityLevel

    def getName(self):
        return self.name
    def getEmail(self):
        return self.email
    def getSecurityLevel(self):
        return self.securityLevel
    
    def __str__(self):
        return self.name + "," + self.email