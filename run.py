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

print("Server is Running Now...")

from pyngrok import ngrok

# Open a HTTP tunnel on the default port 80
# <NgrokTunnel: "http://<public_sub>.ngrok.io" -> "http://localhost:80">
http_tunnel = ngrok.connect(8000)

tunnels = ngrok.get_tunnels()


print(tunnels[0].public_url)
print(tunnels[0].api_url)

ngrok_process = ngrok.get_ngrok_process()

try:
    # Block until CTRL-C or some other terminating event
    ngrok_process.proc.wait()
    print("Ngrok Started..\n Visit http://127.0.0.1")
except KeyboardInterrupt:
    print(" Shutting down server.")

    ngrok.kill()
