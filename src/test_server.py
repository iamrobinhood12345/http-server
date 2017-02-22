"""Tests to make sure client and server can communicate via sockets."""


import pytest


REQUESTS = [
    [
        "OK",
        ("GET /teddy/bear.html HTTP/1.1\r\n"
        "Date: Mon, 27 Jul 1884 12:28:53 GMT\r\n"
        "Server: Teddy Bear\r\n"
        "Host:  \r\n")
    ],
    [
        "method",
        ("PUT /teddy/bear.html HTTP/1.1\r\n"
        "Date: Mon, 27 Jul 1884 12:28:53 GMT\r\n"
        "Server: Teddy Bear\r\n"
        "Host:  \r\n")
    ],
    [
        "version",
        ("GET /teddy/bear.html HTTP/1.0\r\n"
        "Date: Mon, 27 Jul 1884 12:28:53 GMT\r\n"
        "Server: Teddy Bear\r\n"
        "Host:  \r\n")
    ],
    [
        "host",
        ("GET /teddy/bear.html HTTP/1.1\r\n"
        "Date: Mon, 27 Jul 1884 12:28:53 GMT\r\n"
        "Server: Teddy Bear\r\n")
    ],
    [
        "format",
        ("GET /teddy/bear.html HTTP/1.1\r\n"
        "Date : Mon, 27 Jul 1884 12:28:53 GMT\r\n"
        "Server: Teddy Bear\r\n"
        "Host:  \r\n")
    ],
]


REQUESTS_RESPONSES = [
    [
        "GET /teddy/bear.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n",
        "HTTP/1.1 200 OK\r\nDate: Mon, 23 May 2005 22:38:34 GMT\r\nServer: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\nLast-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\nEtag: '3f80f-1b6-3e1cb03b'\r\nAccept-Ranges:  none\r\nContent-Length: 438\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<num bytes of content>"
    ],
    [
        "PUT /teddy/bear.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n",
        "HTTP/1.1 405 Method Not Allowed\r\nDate: Mon, 23 May 2005 22:38:34 GMT\r\nServer: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\nLast-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\nEtag: '3f80f-1b6-3e1cb03b'\r\nAccept-Ranges:  none\r\nContent-Length: 438\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<num bytes of content>"
    ],
    [
        "GET /teddy/bear.html HTTP/1.0\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n",
        "HTTP/1.1 403 Forbidden\r\nDate: Mon, 23 May 2005 22:38:34 GMT\r\nServer: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\nLast-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\nEtag: '3f80f-1b6-3e1cb03b'\r\nAccept-Ranges:  none\r\nContent-Length: 438\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<num bytes of content>"
    ],
    [
        "GET /teddy/bear.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\n",
        "HTTP/1.1 417 Expectation Failed\r\nDate: Mon, 23 May 2005 22:38:34 GMT\r\nServer: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\nLast-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\nEtag: '3f80f-1b6-3e1cb03b'\r\nAccept-Ranges:  none\r\nContent-Length: 438\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<num bytes of content>"
    ],
    [
        "GET /teddy/bear.html HTTP/1.1\r\nDate : Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n",
        "HTTP/1.1 400 Bad Request\r\nDate: Mon, 23 May 2005 22:38:34 GMT\r\nServer: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\nLast-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\nEtag: '3f80f-1b6-3e1cb03b'\r\nAccept-Ranges:  none\r\nContent-Length: 438\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<num bytes of content>"
    ],
]


@pytest.mark.parametrize("status, req", REQUESTS)
def test_method_validation(status, req):
    """Test to see if GET requests are valid and any other type of requests are invalid."""
    from server import method_validation
    valid = method_validation(req)
    if status == "method":
        valid = not valid
    assert valid


@pytest.mark.parametrize("status, req", REQUESTS)
def test_version_validation(status, req):
    """Test to see if GET requests are valid and any other type of requests are invalid."""
    from server import version_validation
    valid = version_validation(req)
    if status == "version":
        valid = not valid
    assert valid


@pytest.mark.parametrize("status, req", REQUESTS)
def test_host_validation(status, req):
    """Test to see if GET requests are valid and any other type of requests are invalid."""
    from server import host_validation
    valid = host_validation(req)
    if status == "host":
        valid = not valid
    assert valid


@pytest.mark.parametrize("status, req", REQUESTS)
def test_format_validation(status, req):
    """Test to see if GET requests are valid and any other type of requests are invalid."""
    from server import format_validation
    valid = format_validation(req)
    if status == "format":
        valid = not valid
    assert valid


def test_client_requests_responses_ok():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[0][0]) == REQUESTS_RESPONSES[0][1]


def test_client_requests_responses_method():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[1][0]) == REQUESTS_RESPONSES[1][1]


def test_client_requests_responses_version():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[2][0]) == REQUESTS_RESPONSES[2][1]


def test_client_requests_responses_host():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[3][0]) == REQUESTS_RESPONSES[3][1]


def test_client_requests_responses_format():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[4][0]) == REQUESTS_RESPONSES[4][1]


# @pytest.mark.parametrize("request, response", REQUESTS_RESPONSES)
# def test_client_requests_responses(request, response):
#     """Test client requests to server return correct responses."""
#     from client import client
#     assert client(request) == response
