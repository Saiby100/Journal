import os

path = os.path.dirname(__file__)

class Notes:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

#Writes login information to the accounts file
def create_account(email, username, password):
    if not check_cred(email.upper(), username.upper()) or not check_pass(password):
        return False

    with open(os.path.join(path, 'resources/account_info.txt'), 'a') as file:
        file.write(email.upper()+','+username.upper()+','+password+'\n')

    return True

#Checks if email or username is being used
def check_cred(user_email, name):
    with open(os.path.join(path, 'resources/account_info.txt'), 'r') as file:
        lines = file.readlines()
        for line in lines:
            email, username, password = line.split(',')
            if user_email == email or name == username:
                return False
    return True

#Checks if password meets criteria
def check_password(password):
    # 8 Characters
    if len(password) < 8:
        print("Password must contain at least 8 characters")
        return False

    # Check for spaces
    if password.__contains__(' '):
        print('Password cannot contain spaces')
        return False

    # Number
    for char in password:
        if char.isnumeric():
            return True
        if char == password[len(password)-1]:
            return False
    return True

#Checks login information
def login(username, password):
    with open(os.path.join('resources/account_info.txt'), 'r') as file:
        for value in file:
            a, b, c = value.split(",")
            c = c.strip("\n")
            if b == username.upper() and c == password:
                return True
    return False
