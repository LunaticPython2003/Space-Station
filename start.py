import os
import json
import time
import pyttsx3 ## text to speech module for python.
import base64
import os
from cryptography.fernet import Fernet

current_path = os.path.abspath(__file__)
dname = os.path.dirname(current_path)
os.chdir(dname)

engine = pyttsx3.init()
os.system("clear")
rate = engine.getProperty('rate')
engine.say("Hello and welcome to the login page of the ISS. I'm Python and the whole program has been possible only coz of me. My current speaking rate is"+str(rate)+". Please wait while I start decryption")
engine.runAndWait()

engine.say("Heelo, please enter the password to decrypt the login file. Remember, the password for decryption is same as passsword for encryption. In case you've deleted the encrypted file, the password you enter here will be used to encrypt the file and will also be the pass for decryption thereafter.")
engine.runAndWait()
from key import getkey
key = getkey()

def decrypt():
    print("beginning decryption")

    input_file = 'data.enc'
    output_file = 'data.json'
    with open(input_file, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    os.remove('data.enc')

if os.path.exists('data.enc'):
    decrypt()

if os.path.exists('data.json'):     ## Checks if the file is decrypted
    print("File decrypted, proceeding with the program.")
    time.sleep(1)
else:
    print("Password is wrong! Please start the process all over.")
    exit()

with open('data.json') as f:
    Users = json.load(f)

def MainMenu():
    status = int(input("Press 1 if you are a new user \nIf you are an old user, press 2 \nPress 3 to quit \nMake your choice: "))
    if status == 1:
        newUser()
    elif status == 2:
        oldUser()
    else:
        exit()

def Done():
    
    engine.say("Thank you for logging in. I'm starting the program in a few seconds.")
    engine.runAndWait()
    from encrypt import start
    start(key)
    f = open('start.status', 'a')
    f.write("Done")
    f.close()
    os.system("python3 space.py")

def newUser():
    login = input("Enter a login name: ")
    if login in Users:
        engine.say("You already exist on our database, "+login+" I'm redirecting you to the login page.")
        engine.runAndWait()
        oldUser()
    else:
        create = input("Enter the password you want to set for the user: ")
        Users[login] = create
        with open('data.json', 'w') as f:
            json.dump(Users, f)
        engine.say("Hey, "+login+"I've created the account. You'll be redirected to the program within a minute")
        engine.runAndWait()
        Done()

def oldUser():
    login = input("Enter your login name: ")
    w = input("Enter your word: ")
    if login in Users and Users[login] == w:
        engine.say("Hello, "+login+", you have suceessfuly logged on. Please wait while I start the program.")
        time.sleep(2)
        Done()
    else:
        engine.say("User does not exist, please start all over. ")
        newUser()

MainMenu()
