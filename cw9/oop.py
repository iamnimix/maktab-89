import re

class User:
    users = dict()

    def __init__(self, name, email, phone, username, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

    @staticmethod
    def validate_email(email):
        if re.match(r'^[\w\.]+@\w+\.\w+', email):
            return email

    @staticmethod
    def validate_phone(phone):
        if re.match(r'^\+98\d{10}$', phone):
            return phone

    @staticmethod
    def validate_password(password):
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password):
            return password

    @classmethod
    def validate_username(cls, username):
        if username not in cls.users:
            return username

    @classmethod
    def register(cls, name, email, phone, username, password):
        new_user = User(name, email, phone, username, password)
        cls.users[username] = new_user
        return new_user

    @classmethod
    def login(cls, username, password):
        try:
            assert username in cls.users.keys() and cls.users[
                username].password == password
            return cls.users[username]
        except AssertionError:
            print("Invalid username or password!!!")


class Main:
    def __init__(self):
        pass

    while True:
        order = input("Enter 1 register, 2 login, 3 exit: ")
        if order == "1":
            name = input("Enter your name: ")

            email = input("Enter your email: ")
            while not User.validate_email(email):
                email = input("valid format for email is: abc12edf@abc.abc: ")

            phone = input("Enter your phone number: ")
            while not User.validate_phone(phone):
                phone = input("Enter a valid phone: ")

            username = input("Enter your username: ")
            while not User.validate_username(username):
                username = input("Enter another username")

            password = input("Enter password: ")
            while not User.validate_password(password):
                password = input("Enter a valid password: ")

            User.register(name, email, phone, username, password)

        elif order == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            logged_user = User.login(username, password)
            if logged_user:
                print(f"Welcome {logged_user.name} with phone {logged_user.phone}")
            else:
                print("")

        elif order == "3":
            break


Main()
