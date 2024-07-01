import getpass
import hashlib
import json
import os
from app.todo import (load_users, save_users)


#### User Registration Start Here ####

DATA_DIR = 'data'
USER_FILE = os.path.join(DATA_DIR, 'user.json')

def register():
    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    users = load_users()
    if username in users:
        print("User already exists. Please Login.")
        return
    users[username] = hashed_password
    save_users(users)
    print("Registration successful.")

def login():
    username = input("Enter Your Username: ")
    password = getpass.getpass("Enter Your Password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    users = load_users()
    if username not in users or users[username] != hashed_password:
        print("Invalid username or password.")
        return None
    print("Login successful.")
    return username

#### User Registration End Here ####