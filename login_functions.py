import os

path = os.path.dirname(__file__)

class Notes:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

#Writes login information to the accounts file if
def create_account(email, username, password):
    with open(os.path.join(path, 'resources/account_info.txt'), 'a') as file:
        file.write(email.upper()+','+username.upper()+','+password+'\n')


#Checks if email or username is being used
def check_cred(user_email, name, input_password, conf_password):


    if len(user_email) == 0 or len(name) == 0 or user_email.__contains__(' ') or name.__contains__(' '):
        return 'Fields cannot be left blank'

    if not user_email.__contains__('@gmail.com'):
        return 'Invalid email'

    with open(os.path.join(path, 'resources/account_info.txt'), 'r') as file:
        lines = file.readlines()
        for line in lines:
            email, username, password = line.split(',')
            if user_email.upper() == email or name.upper() == username:
                return 'email or username is already in use'

    return check_password(input_password, conf_password)

#Checks if password meets criteria
def check_password(password, conf_password):
    # 8 Characters
    if len(password) < 8:
        return 'Password must contain at least 8 characters'

    # Check for spaces
    if password.__contains__(' '):
        return 'Password cannot contain spaces'

    # Number
    for char in password:
        if char.isnumeric():
            break
        if char == password[len(password)-1]:
            return 'Password must contain at least one number'

    if password != conf_password:
        return 'Passwords do not match'

    return 'Successfully Registered!'

#Checks login information
def login(username, password):
    with open(os.path.join('resources/account_info.txt'), 'r') as file:
        for value in file:
            a, b, c = value.split(",")
            c = c.strip("\n")
            if b == username.upper() and c == password:
                return True
    return False
