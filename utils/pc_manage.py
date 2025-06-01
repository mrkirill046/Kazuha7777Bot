import logging
import os

def reboot():
    logging.info("Rebooting...")
    os.system("sudo /usr/bin/reboot")

def shutdown():
    logging.info("Shutting down...")
    os.system("sudo /usr/bin/shutdown now")
