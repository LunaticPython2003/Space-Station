from cryptography.fernet import Fernet
import os

current_path = os.path.abspath(__file__)
dname = os.path.dirname(current_path)
os.chdir(dname)

def start(key):
    input_file = './data.json'
    output_file = './data.enc'
    with open(input_file, 'rb') as f:
        data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    os.system("rm -rf ./"+input_file)
    os.system("clear")

if __name__ == "__main__":
    start(key)
