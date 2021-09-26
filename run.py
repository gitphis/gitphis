import os 
import subprocess
import sys
import threading

def runserver():
    os.system("python manage.py runserver")
    print("running")


x = threading.Thread(target=runserver)
# x.start()
# x.join()

x.daemon = True                            # Daemonize thread
x.start()  

print("Server is Running Now")
