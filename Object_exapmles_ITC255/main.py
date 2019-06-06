""" from user import User
def setUser():
    u=User('Sue', 's@gmail.com', 'high')
    print(u)
def main():
    setUser()
main()
 """


from staff import Staff
def setUser():
    s = Staff('Sue', 's@gmail.com', 'high', 'Manager')
    print(s.getEmail())
    print(s.getName())
    print(s.getSecurityLevel())

    print(s)
def main():
    setUser()
main()
