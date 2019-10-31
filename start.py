import os
import json
import time
import pyttsx3     ## text to speech module for python. Requires espeak in Mac OS/Linux

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 110)      ## Defines the speed
engine.say('''Hello user and welcome to the login page! The program has been created using me, python.
Please proceed through the login page to start the program. My speaking rate is ''' +str(rate))
engine.runAndWait()
print("Hello")

password = input("Enter the password to open decrypt login file.")
os.system("openssl enc -aes-256-cbc -d -in data.enc -out data.json -k "+password)    ## Decrypts the file using openssl

if os.path.exists('data.json'):     ## Checks if the file is decrypted
    print("File decrypted, proceeding with the program.")
    time.sleep(1)
    os.remove('data.enc')
else:
    print("Password specified is wrong! Please start the process all over.")
    quit()

with open('data.json')as f:
    Users = json.load(f)

status = ""

def MainMenu():
    global status
    status = input("Press Y if you are a new user \nIf you are an old user \nPress q to quit")
    if status == "y" or "Y":
        newUser()
    elif status == "n" or "N":
        oldUser()
    else:
         quit()

def Done():
    engine.say("Hello, please wait while I redirect you to the program. Encrypting the file. Thanks for having patience.")
    engine.runAndWait()
    os.system("openssl enc -aes-256-cbc -d -in data.enc -out data.json -k " +password)
    os.remove('data.json')
    os.system("python3 space.py")

def newUser():
    login = input("Enter a login name: ")
    if login in Users:
        engine.say("You already exist on our database "+login+" I'm redirecting you to the login page.")
        engine.runAndWait()
        oldUser()
    else:
        createPass = input("Enter the password you want to set for the user: ")
        Users[login] = createPass
        with open('data.json', 'w') as f:
            json.dump(Users, f)
        engine.say("Hey, "+login+"I've created the account. You'll be redirected to the program within a minute")
        engine.runAndWait()
        Done()

def oldUser():
    login = input("Enter your login name: ")
    passw = input("Enter your password: ")
    if login in Users and Users[login] == passw:
        engine.say("Hello, "+login+"you have suceessfuly logged on to. Please wait while I start the program.")
        Done()
    else:
        engine.say("User does not exist, please start all over. ")
        oldUser()

MainMenu()
