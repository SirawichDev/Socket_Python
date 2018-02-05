import socket

def con():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("192.168.1.101",8080))
    soc.listen(1)
    conn,addr = soc.accept()
    print ('Got Connect From :'), addr

    while True:
        command =input("CMD >> ")

        if 'terminate' in command:
            conn.send('terminate')
            conn.close() #cloase connect with Host
            break
        
        
        else:
            conn.send(command)
            print (conn.recv(1024))

def main():
    con()
main()