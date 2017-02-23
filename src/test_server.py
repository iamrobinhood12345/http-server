# encoding:utf-8

"""Tests to make sure client and server can communicate via sockets."""


import pytest

OK_PARAMS = [
    ("GET th® blerg woot"),
    ("GET thü blerg woot"),
    ("GET thñ blerg woot"),
    ("GET th® blerg woot"),
    ("GET the blerg woot"),
    ("GET I eat  éclaires"),
    ("GET é®ñü®")
]

FAILED_PARAMS = [
    ("Get th® blerg woot"),
    ("Get thü blerg woot"),
    ("Get thñ blerg woot"),
    ("Get th® blerg woot"),
    ("Get the blerg woot"),
    ("Get I eat  éclaires"),
    ("Get é®ñü®")
]


@pytest.mark.parametrize("n", OK_PARAMS)
def test_response_ok(n):
    """Test to see if valid client request will return a 200 OK message."""
    from client import client
    response = ("HTTP/1.1 200 OK\r\n"
        "Server: Teddy Bear\r\n"
        "Content-Type: text/html\r\n"
        "Connection: Closed\r\n\r\n"
        "<html>\r\n"
        "<body>\r\n"
        "<h1>Hello, World!</h1>\r\n"
        "</body>\r\n"
        "</html>")
    assert client(n) == response


@pytest.mark.parametrize("n", FAILED_PARAMS)
def test_response_failed(n):
    """Test to see if invalid client request will return a 500 Error message."""
    from client import client
    response = ("HTTP/1.1 500 Internal Server Error\r\n"
        "Server: Teddy Bear\r\n"
        "Content-Type: text/html\r\n"
        "Connection: Closed\r\n\r\n"
        "<html>\r\n"
        "<body>\r\n"
        "<h1>Internal Server Error</h1>\r\n"
        "</body>\r\n"
        "</html>")
    assert client(n) == response


def test_method_validation_ok():
    """Test correct method."""
    from server import method_validation
    assert method_validation("GET ") is True


def test_method_validation_error():
    """Test incorrect method."""
    from server import method_validation
    assert method_validation("get ") is False
