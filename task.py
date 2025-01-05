import hashlib
import os
import json
import base64


def createsalt(length=12):
    return os.urandom(length)

def hash(password, salt):
   
    combined = salt + password.encode()
    hashed = hashlib.sha256(combined).hexdigest()
    return hashed


task=input("click 1 for login and 2 for sign up\n")

if task=="2":
    username=input("enter the user name\n")
    password=input("please enter the password\n")

    salt = createsalt()
    hashed = hash(password,salt)

    file_path = "data.json"

    with open(file_path, "r") as file:
        data = json.load(file)  # Load JSON data into a dictionary

    salt_64 = base64.b64encode(salt).decode()


    data["userid"][username] = {
        "salt": salt_64,
        "hash": hashed
    }

    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        
    print("User "+ username+" added successfully.")


if task=="1":
    username=input("Enter the username")
    password=input("enter password")


    file_path = "data.json"

    with open(file_path, "r") as file:
        data = json.load(file)  # Load JSON data into a dictionary


    salted= data["userid"][username]["salt"]
    
    
    salt = base64.b64decode(salted)
    hashed=hash(password,salt)
    #salt=base64.b64encode(salt).decode()

    if data["userid"][username]["hash"] == hashed:
        print("login succesfull")
    else:
        print("login failed")