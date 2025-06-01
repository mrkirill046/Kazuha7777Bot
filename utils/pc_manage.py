import os

def reboot():
    os.system("sudo /usr/bin/reboot")

def shutdown():
    os.system("sudo /usr/bin/shutdown now")
