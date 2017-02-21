"""Server programmed to echo messages from client."""


import socket
import sys


def server():
    """Recieve a message from the client and echos it back."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ("127.0.0.1", 5017)
    server_socket.bind(address)
    server_socket.listen(3)
    conn, addr = server_socket.accept()
    buffer_length = 8
    message_complete = False
    response = u""
    while not message_complete:
        data = conn.recv(buffer_length)
        response += data.decode('utf8')
        if len(data) < buffer_length:
            break
    conn.sendall(response.encode('utf8'))
    conn.close()
    server_socket.close()
    return response

if __name__ == '__main__':
    """Run server from command line."""
    server()
