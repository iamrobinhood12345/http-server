"""Client for communicating with http server."""


import socket
import sys


def client(message):
    """Create the protocol for interacting with server."""
    if len(message) % 8 == 0:
        message += '$'
    info = socket.getaddrinfo('127.0.0.1', 7000)
    stream_info = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client_socket = socket.socket(*stream_info[:3])
    client_socket.connect(stream_info[-1])
    buffer_length = 8
    response = ""
    print(message.encode('utf-8'))
    client_socket.sendall(message.encode('utf-8'))
    response_list = []
    while True:
        data = client_socket.recv(buffer_length).decode('utf-8')
        response_list.append(data)
        if len(data) < buffer_length:
            break
    client_socket.close()
    response = ''.join(response_list)
    print(response)
    return response


if __name__ == "__main__":
    client(sys.argv[1])
