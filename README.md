# http-server

An http server using python sockets.

## Tox:

    src/test_server.py .F..

    ---------- coverage: platform darwin, python 3.5.2-final-0 -----------
    Name                 Stmts   Miss  Cover   Missing
    --------------------------------------------------
    src/client.py           24      3    88%   11, 19, 32
    src/server.py           40     31    22%   11-37, 47-56, 61-70, 74
    src/test_server.py      15      0   100%
    --------------------------------------------------
    TOTAL                   79     34    57%
    
Can only run one server test at a time on my system. Connection does not close.




## Usage with changing port numbers between uses:

### "200 OK" request/response cycle (valid request):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python client.py "GET /teddy/bear.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8
    
#### Python2:

    <num bytes of content>
    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET /teddy/bear.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <num bytes of content>
    
### "405 Method Not Allowed" request/response cycle (incorrect method):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python3 client.py "PUT /teddy/bear.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 405 Method Not Allowed
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <num bytes of content>
    
#### Python2:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "PUT /teddy/bear.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 405 Method Not Allowed
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <num bytes of content>
    
### "403 Forbidden" request/response cycle (incorrect version):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python3 client.py "GET /teddy/bear.html HTTP/1.0\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 403 Forbidden
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <num bytes of content>
    
#### Python2:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET /teddy/bear.html HTTP/1.0\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 403 Forbidden
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <num bytes of content>

### "417 Expectation Failed" request/response cycle (incorrect host):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python3 client.py "GET /teddy/bear.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\n"
    HTTP/1.1 417 Expectation Failed
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <num bytes of content>
    
#### Python2:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET /teddy/bear.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\n"
    HTTP/1.1 417 Expectation Failed
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <num bytes of content>
    
### "400 Bad Request" request/response cycle (incorrect format):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python3 client.py "GET /teddy/bear.html HTTP/1.1\r\nDate : Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 400 Bad Request
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <num bytes of content>
    
#### Python2:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET /teddy/bear.html HTTP/1.1\r\nDate : Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 400 Bad Request
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 438
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <num bytes of content>
