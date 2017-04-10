
"""Server programmed to recieve messages from client and return http response."""


import socket
import sys


def server():
    """Recieve a message from the client and echos it back."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server_socket.bind(("127.0.0.1", 6024))
    server_socket.listen(1)
    buffer_length = 8
    while True:
        conn, addr = server_socket.accept()
        message_complete = False
        request = u""
        while not message_complete:
            addition = conn.recv(buffer_length)
            request += addition.decode('utf-8')
            if len(addition) < buffer_length:
                break
        print(request)
        if method_validation(request):
            message = response_ok()
            if sys.version_info[0] == 2:
                message = message.decode('utf-8')
            conn.sendall(message.encode('utf-8'))
        else:
            message = response_error()
            if sys.version_info[0] == 2:
                message = message.decode('utf-8')
            conn.sendall(message.encode('utf-8'))
        conn.close()


def method_validation(request):
    """Verify method."""
    return request[:4] == u"GET "


def response_ok():
    """Return 200 OK response."""
    response = ("HTTP/1.1 200 OK\r\n"
        "Server: Teddy Bear\r\n"
        "Content-Type: text/html\r\n"
        "Connection: Closed\r\n\r\n"
        "<html>\r\n"
        "<body>\r\n"
        "<h1>Hello, World!</h1>\r\n"
        "</body>\r\n"
        "</html>")
    return response


def response_error():
    """Return 500 Internal Server Error response."""
    response = ("HTTP/1.1 500 Internal Server Error\r\n"
        "Server: Teddy Bear\r\n"
        "Content-Type: text/html\r\n"
        "Connection: Closed\r\n\r\n"
        "<html>\r\n"
        "<body>\r\n"
        "<h1>Internal Server Error</h1>\r\n"
        "</body>\r\n"
        "</html>")
    return response

if __name__ == '__main__':
    """Run server from command line."""
    server()
