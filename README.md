# http-server

An http server using python sockets.

## Tox:

        platform darwin -- Python 3.5.2, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
        rootdir: /Users/ben/401/http-server2/http-server, inifile: 
        plugins: cov-2.4.0
        collected 27 items 

        src/test_server.py ....................FFFFFFF

        ---------- coverage: platform darwin, python 3.5.2-final-0 -----------
        Name                 Stmts   Miss  Cover   Missing
        --------------------------------------------------
        src/client.py           27     17    37%   16-33, 37
        src/server.py           92     58    37%   10-25, 30-36, 41-51, 79, 84, 92, 98-116, 121-178, 183
        src/test_server.py      49      0   100%
        --------------------------------------------------
        TOTAL                  168     75    55%
  
-

        platform darwin -- Python 2.7.13, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
        rootdir: /Users/ben/401/http-server2/http-server, inifile: 
        plugins: cov-2.4.0
        collected 27 items 

        src/test_server.py .....................FFFFFF

        ---------- coverage: platform darwin, python 2.7.13-final-0 ----------
        Name                 Stmts   Miss  Cover   Missing
        --------------------------------------------------
        src/client.py           27      3    89%   21, 28, 37
        src/server.py           92     58    37%   10-25, 30-36, 41-51, 79, 84, 92, 98-116, 121-178, 183
        src/test_server.py      49      0   100%
        --------------------------------------------------
        TOTAL                  168     61    64%
    
Can only run one server test at a time on my system. Connection does not close.




## "Console Tests" with changing port numbers between uses:

### "200 OK" request/response cycle (valid request, "GET webroot"):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python3 client.py "GET webroot HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 114
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <html><body><ul><li>a_web_page.html</li><li>images</li><li>make_time.py</li><li>sample.txt</li></ul></body></html>
    
#### Python2:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET webroot HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 114
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <html><body><ul><li>a_web_page.html</li><li>images</li><li>make_time.py</li><li>sample.txt</li></ul></body></html>

### "200 OK" request/response cycle (valid request, "GET webroot/images"):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python3 client.py "GET webroot/images HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 112
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <html><body><ul><li>JPEG_example.jpg</li><li>sample_1.png</li><li>Sample_Scene_Balls.jpg</li></ul></body></html>
    
#### Python2:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET webroot/images HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 112
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <html><body><ul><li>JPEG_example.jpg</li><li>sample_1.png</li><li>Sample_Scene_Balls.jpg</li></ul></body></html>

### "200 OK" request/response cycle (valid request, "GET webroot/a_web_page.html"):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python3 client.py "GET webroot/a_web_page.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 123
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <!DOCTYPE html>
    <html>
    <body>

    <h1>Code Fellows</h1>

    <p>A fine place to learn Python web programming!</p>

    </body>
    </html>
    
#### Python2:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET webroot/a_web_page.html HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 123
    Connection: close
    Content-Type: text/html; charset=UTF-8

    <!DOCTYPE html>
    <html>
    <body>

    <h1>Code Fellows</h1>

    <p>A fine place to learn Python web programming!</p>

    </body>
    </html>

### "200 OK" request/response cycle (valid request, "GET webroot/make_time.py"):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python3 client.py "GET webroot/make_time.py HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 278
    Connection: close
    Content-Type: text/html; charset=UTF-8

    #!/usr/bin/env python

    """
    make_time.py

    simple script that returns and HTML page with the current time
    """

    import datetime

    time_str = datetime.datetime.now().isoformat()

    html = """
    <http>
    <body>
    <h2> The time is: </h2>
    <p> %s <p>
    </body>
    </http>
    """ % time_str

    print(html)

    
#### Python2:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET webroot/make_time.py HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 278
    Connection: close
    Content-Type: text/html; charset=UTF-8

    #!/usr/bin/env python

    """
    make_time.py

    simple script that returns and HTML page with the current time
    """

    import datetime

    time_str = datetime.datetime.now().isoformat()

    html = """
    <http>
    <body>
    <h2> The time is: </h2>
    <p> %s <p>
    </body>
    </http>
    """ % time_str

    print(html)


### "200 OK" request/response cycle (valid request, "GET webroot/sample.txt"):

#### Python3:

    (env) Williams-MacBook-Pro:src ben$ python3 client.py "GET webroot/sample.txt HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 94
    Connection: close
    Content-Type: text/html; charset=UTF-8

    This is a very simple text file.
    Just to show that we can serve it up.
    It is three lines long.
    
#### Python2:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET webroot/sample.txt HTTP/1.1\r\nDate: Mon, 27 Jul 1884 12:28:53 GMT\r\nServer: Teddy Bear\r\nHost:  \r\n"
    HTTP/1.1 200 OK
    Date: Mon, 23 May 2005 22:38:34 GMT
    Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
    Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
    Etag: '3f80f-1b6-3e1cb03b'
    Accept-Ranges:  none
    Content-Length: 94
    Connection: close
    Content-Type: text/html; charset=UTF-8

    This is a very simple text file.
    Just to show that we can serve it up.
    It is three lines long.

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
