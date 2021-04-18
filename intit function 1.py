class User:
    def __init__(self, name, email, contact):
        self.name=name;
        self.email=email;
        self.contact=contact;


user=User("Pratik","pratikshte@gamil.com",22)
print(user.name,end=" ")
print(user.email,end=" ")
print(user.contact)
