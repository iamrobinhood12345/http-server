
"""Server programmed to recieve messages from client and return http response."""


import socket
import sys


def server():
    """Recieve a message from the client and sends a response back."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server_socket.bind(("127.0.0.1", 7032))
    server_socket.listen(1)
    buffer_length = 8
    while True:
        conn, addr = server_socket.accept()
        req = buffer_request(buffer_length, conn)
        print(req)
        message = parse_request(req)
        if sys.version_info[0] == 2:
            conn.sendall(message)
        else:
            conn.sendall(message.encode('utf-8'))
        conn.close()


def buffer_request(buffer_length, conn):
    """Return a decoded client request."""
    req = u""
    while True:
        addition = conn.recv(buffer_length).decode('utf-8')
        req += addition
        if len(addition) < buffer_length:
            break
    return req.replace('\\r\\n', '\r\n')


def parse_request(request):
    """Return a server response based on client request formatting."""
    if not method_validation(request):
        return response_error("method")
    elif not version_validation(request):
        return response_error("version")
    elif not host_validation(request):
        return response_error("host")
    elif not format_validation(request):
        return response_error("format")
    uri = request.split(" ", 2)[1]
    info = resolve_uri(uri)
    return response_error("OK", info[0], info[1])


def method_validation(request):
    """Verify method formatting and type."""
    return request[:4] == u"GET "


def version_validation(request):
    """Verify version formatting and type."""
    return request.split(' ')[2][:8] == u"HTTP/1.1"


def host_validation(request):
    """Verify host formatting and type."""
    return request.split('\r\n')[3] == u"Host:  "


def format_validation(request):
    """Verify format formatting and type."""
    val_count = 0
    for ind in range(len(request)):
        if val_count == 0 or val_count == 1:
            if request[ind] == u" ":
                val_count += 1
            elif request[ind:ind + 1] == u"\r\n":
                return False
        elif val_count == 2:
            if request[ind:ind + 2] == u"\r\n":
                val_count += 1
            elif request[ind] == u" ":
                return False
        elif val_count % 2 == 1:
            if request[ind] == u":":
                val_count += 1
            elif request[ind] == u" ":
                return False
        else:
            if request[ind] == u"\r\n":
                val_count += 1
    return True


def resolve_uri(uri):
    """Uri determines response body content."""
    import io
    import os
    if os.path.isdir(uri):
        content_type = ".dir"
        fials = os.listdir(uri)
        center = "</li><li>".join(fials)
        body = "<html><body><ul><li>" + center + "</li></ul></body></html>"
    else:
        ind = uri.index(".")
        content_type = uri[ind:]
        if content_type == ".jpg" or content_type == ".png":
            fial = io.open(uri, "rb")
            body = str(fial.read())
        else:
            fial = io.open(uri, "r")
            body = fial.read()
        fial.close()
    return body, content_type


def response_error(key, body=None, content_type=None):
    """Return evaluated request resopnse, either OK or a specific response error."""
    response_dict = {
        "method": ("HTTP/1.1 405 Method Not Allowed\r\n"
                    "Date: Mon, 23 May 2005 22:38:34 GMT\r\n"
                    "Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n"
                    "Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n"
                    "Etag: '3f80f-1b6-3e1cb03b'\r\n"
                    "Accept-Ranges:  none\r\n"
                    "Content-Length: 438\r\n"
                    "Connection: close\r\n"
                    "Content-Type: text/html; charset=UTF-8\r\n"
                    "\r\n"
                    "<num bytes of content>"),
        "version": ("HTTP/1.1 403 Forbidden\r\n"
                    "Date: Mon, 23 May 2005 22:38:34 GMT\r\n"
                    "Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n"
                    "Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n"
                    "Etag: '3f80f-1b6-3e1cb03b'\r\n"
                    "Accept-Ranges:  none\r\n"
                    "Content-Length: 438\r\n"
                    "Connection: close\r\n"
                    "Content-Type: text/html; charset=UTF-8\r\n"
                    "\r\n"
                    "<num bytes of content>"),
        "host": ("HTTP/1.1 417 Expectation Failed\r\n"
                    "Date: Mon, 23 May 2005 22:38:34 GMT\r\n"
                    "Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n"
                    "Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n"
                    "Etag: '3f80f-1b6-3e1cb03b'\r\n"
                    "Accept-Ranges:  none\r\n"
                    "Content-Length: 438\r\n"
                    "Connection: close\r\n"
                    "Content-Type: text/html; charset=UTF-8\r\n"
                    "\r\n"
                    "<num bytes of content>"),
        "format": ("HTTP/1.1 400 Bad Request\r\n"
                    "Date: Mon, 23 May 2005 22:38:34 GMT\r\n"
                    "Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n"
                    "Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n"
                    "Etag: '3f80f-1b6-3e1cb03b'\r\n"
                    "Accept-Ranges:  none\r\n"
                    "Content-Length: 438\r\n"
                    "Connection: close\r\n"
                    "Content-Type: text/html; charset=UTF-8\r\n"
                    "\r\n"
                    "<num bytes of content>"),
    }
    if key == "OK":
        response_dict[key] = ("HTTP/1.1 200 OK\r\n"
            "Date: Mon, 23 May 2005 22:38:34 GMT\r\n"
            "Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\n"
            "Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\n"
            "Etag: '3f80f-1b6-3e1cb03b'\r\n"
            "Accept-Ranges:  none\r\n"
            "Content-Length: " + str(len(body)) + "\r\n"
            "Connection: close\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n"
            "\r\n" + body)
    return response_dict[key] if key in response_dict else response_dict['format']

if __name__ == '__main__':
    server()
