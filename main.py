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
def pip():
    print("Installing pip dependencies...")
    os.system("python -m pip install pyttsx3 geocoder")
    os.system("clear")
    print("All dependencies satisfied, starting the program now!")
if os.name == "posix":
    print("Linux/Mac OS system detected, proceeding with the program")
    time.sleep (5)
    os.system("clear")
    current_path = os.path.abspath(__file__)
    dname = os.path.dirname(current_path)
    os.chdir(dname)
    if sys.platform == "Linux" or sys.platform == "linux":
        print("Currently only Debian based distributions of Linux are supported. You'll get an error otherwise")
        os.system("sudo apt install espeak")
        os.system("clear")
        pip()
        print("Dependencies installed, starting the program.")
        time.sleep(2)
        os.system("python3 ./start.txt")
    elif sys.platform == "Darwin" or sys.platform == "darwin":
        print("Mac OS apparently has all the dependencies needed and therefore only pip installs are to be done")
        time.sleep(2)
        os.system("clear")
        pip()
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


