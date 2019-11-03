import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

current_path = os.path.abspath(__file__)
dname = os.path.dirname(current_path)
os.chdir(dname)

key = ""

def getkey():
    password_provided = input("Enter your password") # This is input in the form of a string
    password = password_provided.encode() # Convert to type bytes
    salt = b'salt_'
    kdf = PBKDF2HMAC(
                 algorithm=hashes.SHA256(),
                 length=32,
                 salt=salt,
                 iterations=100000,
                 backend=default_backend()
                 )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    os.system("clear")
    return key

if __name__ == "__main__":
    getkey()
