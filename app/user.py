import getpass
import bcrypt
import json
import os


#### User Registration and Login Start Here ####

DATA_DIR = 'data'
USER_FILE = os.path.join(DATA_DIR, 'users.json')

def load_users():
    try:
        if not os.path.exists(USER_FILE):
            return {}
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def register():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as file:
            json.dump({}, file)

    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")

    users = load_users()
    if username in users:
        print("User already exists. Please Login.")
        return

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    users[username] = hashed_password
    save_users(users)
    print("Registration successful.")

def login():
    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")

    users = load_users()
    if username not in users:
        print("Invalid username or password.")
        return None

    hashed_password = users[username].encode('utf-8')

    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print("Login successful.")
        return username
    else:
        print("Invalid username or password.")
        return None

#### User Registration and Login End Here ####
