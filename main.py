## This python script checks for the build section and installs dependencies automatically (if required) and stops
## the program if unknown/unsupported system is detected

import time
import os
import sys

print ('''░█──░█ █▀▀ █── █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▀▀█▀▀ █──█ █▀▀ 
░█░█░█ █▀▀ █── █── █──█ █─▀─█ █▀▀ 　 ──█── █──█ 　 ──█── █▀▀█ █▀▀ 
░█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀───▀ ▀▀▀ 　 ──▀── ▀▀▀▀ 　 ──▀── ▀──▀ ▀▀▀ ''')
print ('''─▀─ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▀█ ▀▀█▀▀ ─▀─ █▀▀█ █▀▀▄ █▀▀█ █── 　 
▀█▀ █──█ ──█── █▀▀ █▄▄▀ █──█ █▄▄█ ──█── ▀█▀ █──█ █──█ █▄▄█ █── 　 
▀▀▀ ▀──▀ ──▀── ▀▀▀ ▀─▀▀ ▀──▀ ▀──▀ ──▀── ▀▀▀ ▀▀▀▀ ▀──▀ ▀──▀ ▀▀▀ 　 ''')
print ('''█▀▀ █▀▀█ █▀▀█ █▀▀ █▀▀ 　 █▀▀ ▀▀█▀▀ █▀▀█ ▀▀█▀▀ ─▀─ █▀▀█ █▀▀▄ 
▀▀█ █──█ █▄▄█ █── █▀▀ 　 ▀▀█ ──█── █▄▄█ ──█── ▀█▀ █──█ █──█ 
▀▀▀ █▀▀▀ ▀──▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ──▀── ▀──▀ ──▀── ▀▀▀ ▀▀▀▀ ▀──▀ ''')

time.sleep(5)
if os.name == "posix":
    print("Linux/Mac OS system detected, proceeding with the program")
    time.sleep (5)
    os.system("clear")
    current_path = os.path.abspath(__file__)
    dname = os.path.dirname(current_path)
    os.chdir(dname)
    if sys.platform == "Linux" or sys.platform == "linux":
        print("Currently only Debian based distributions of Linux are supported. You'll get an error otherwise")
        os.system("sudo apt install openssl")
        os.system("clear")
        os.system("sudo apt install espeak")
        print("Dependencies installed, starting the program.")
        time.sleep(2)
        os.system("python3 ./start.txt")
    elif sys.platform == "Darwin" or sys.platform == "darwin":
        print("Running setup for Mac OS. Make sure you have homebrew installed.")
        os.system("brew install openssl")
        os.system("clear")
        print("Dependencies installed, starting the program")
        time.sleep(2)
        os.system("python3 ./start.py")
elif os.name == "nt":
    os.system("cls")
    print("Windows is not supported now as it does not have Unix commands. Please consider")
    print("using WSL on Windows 10 or cygwin on Windows 7-8.1")
    time.sleep(5)
    os.system("cls")
else:
    print("System type not recognized. Please consider using Mac OS/Linux or WSL/Cygwin. ")
    print("Exiting thr program..")
    exit()


