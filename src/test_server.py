# encoding:utf-8

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
    [
        "GET webroot HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n",
        "HTTP/1.1 200 OK\r\nDate: Mon, 23 May 2005 22:38:34 GMT\r\nServer: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\nLast-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\nEtag: '3f80f-1b6-3e1cb03b'\r\nAccept-Ranges:  none\r\nContent-Length: 114\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<html><body><ul><li>a_web_page.html</li><li>images</li><li>make_time.py</li><li>sample.txt</li></ul></body></html>"
    ],
    [
        "GET webroot/images HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n",
        "HTTP/1.1 200 OK\r\nDate: Mon, 23 May 2005 22:38:34 GMT\r\nServer: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\nLast-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\nEtag: '3f80f-1b6-3e1cb03b'\r\nAccept-Ranges:  none\r\nContent-Length: 112\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<html><body><ul><li>JPEG_example.jpg</li><li>sample_1.png</li><li>Sample_Scene_Balls.jpg</li></ul></body></html>"
    ],
    [
        "GET webroot/sample.txt HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n",
        "HTTP/1.1 200 OK\r\nDate: Mon, 23 May 2005 22:38:34 GMT\r\nServer: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\r\nLast-Modified: Wed, 08 Jan 2003 23:11:55 GMT\r\nEtag: '3f80f-1b6-3e1cb03b'\r\nAccept-Ranges:  none\r\nContent-Length: 94\r\nConnection: close\r\nContent-Type: text/html; charset=UTF-8\r\n\r\nThis is a very simple text file.\nJust to show that we can serve it up.\nIt is three lines long."
    ],
]


def test_parse_request_method():
    """Test parse_request returns correct responses."""
    from server import parse_request
    assert parse_request(REQUESTS_RESPONSES[0][0]) == REQUESTS_RESPONSES[0][1]


def test_parse_request_version():
    """Test parse_request returns correct responses."""
    from server import parse_request
    assert parse_request(REQUESTS_RESPONSES[1][0]) == REQUESTS_RESPONSES[1][1]


def test_parse_request_host():
    """Test parse_request returns correct responses."""
    from server import parse_request
    assert parse_request(REQUESTS_RESPONSES[2][0]) == REQUESTS_RESPONSES[2][1]


def test_parse_request_format():
    """Test parse_request returns correct responses."""
    from server import parse_request
    assert parse_request(REQUESTS_RESPONSES[3][0]) == REQUESTS_RESPONSES[3][1]


@pytest.mark.parametrize("status, req", REQUESTS)
def test_method_validation(status, req):
    """Test to see if GET requests are valid and any other type of requests are invalid."""
    from server import method_validation
    assert method_validation("GET ") is True


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


def test_client_requests_responses_method():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[0][0]) == REQUESTS_RESPONSES[0][1]


def test_client_requests_responses_version():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[1][0]) == REQUESTS_RESPONSES[1][1]


def test_client_requests_responses_host():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[2][0]) == REQUESTS_RESPONSES[2][1]


def test_client_requests_responses_format():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[3][0]) == REQUESTS_RESPONSES[3][1]


def test_client_requests_response_ok_webroot():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[4][0]) == REQUESTS_RESPONSES[4][1]


def test_client_requests_response_ok_webroot_images():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[5][0]) == REQUESTS_RESPONSES[5][1]


def test_client_requests_response_ok_webroot_sample():
    """Test client requests to server return correct responses."""
    from client import client
    assert client(REQUESTS_RESPONSES[6][0]) == REQUESTS_RESPONSES[6][1]
