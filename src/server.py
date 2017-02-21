"""Server programmed to recieve messages from client and return http response."""


import socket
import sys


def server():
    """Recieve a message from the client and echos it back."""
    while True:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        address = ("127.0.0.1", 6011)
        server_socket.bind(address)
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        buffer_length = 8
        message_complete = False
        response = ""
        sent = False
        while not message_complete:
            addition = conn.recv(buffer_length).decode('utf-8')
            response += addition
            if response == 'bad request':
                conn.sendall(response_error().encode('utf-8'))
                sent = True
                break
            elif len(addition) < buffer_length:
                break
        print(response)
        if not sent:
            conn.sendall(response_ok().encode('utf-8'))
        conn.close()


def response_ok():
    """Return 200 OK response."""
    response = ("HTTP/1.1 200 OK\r\n" +
        "Server: Teddy Bear\r\n" +
        "Content-Type: text/html\r\n" +
        "Connection: Closed\r\n\r\n" +
        "<html>\r\n" +
        "<body>\r\n" +
        "<h1>Hello, World!</h1>\r\n" +
        "</body>\r\n" +
        "</html>")
    return response


def response_error():
    """Return 500 Internal Server Error response."""
    response = ("HTTP/1.1 500 Internal Server Error\r\n" +
        "Server: Teddy Bear\r\n" +
        "Content-Type: text/html\r\n" +
        "Connection: Closed\r\n\r\n" +
        "<html>\r\n" +
        "<body>\r\n" +
        "<h1>Internal Server Error</h1>\r\n" +
        "</body>\r\n" +
        "</html>")
    return response

if __name__ == '__main__':
    """Run server from command line."""
    server()
