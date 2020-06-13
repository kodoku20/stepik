import socket
import os
import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 2222))
server_socket.listen(10)

while True:
    client_socket, remote_address = server_socket.accept()
    child_pid = os.fork()
    if child_pid == 0:
        request = client_socket.recv(1024)
        client_socket.send(request)
        client_socket.close()
        sys.exit()
    else:
        client_socket.close()

server_socket.close()
