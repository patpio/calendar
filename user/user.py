class User:
    def __init__(self, name, email):
        self.email = email
        self.name = name

    def __str__(self):
        return f'class User(name: {self.name}, email: {self.email})'
