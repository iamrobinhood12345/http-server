# http-server

An http server using python sockets.


## Tox:

    src/test_server.py ................

    ---------- coverage: platform darwin, python 3.5.2-final-0 -----------
    Name                 Stmts   Miss  Cover   Missing
    --------------------------------------------------
    src/client.py           24      3    88%   11, 19, 32
    src/server.py           38     29    24%   11-35, 45-54, 59-68, 72
    src/test_server.py      18      0   100%
    --------------------------------------------------
    TOTAL                   80     32    60%


    =================================== 16 passed in 0.13 seconds ====================================
    
-

    src/test_server.py ................

    ---------- coverage: platform darwin, python 2.7.13-final-0 ----------
    Name                 Stmts   Miss  Cover   Missing
    --------------------------------------------------
    src/client.py           24      2    92%   11, 32
    src/server.py           38     29    24%   11-35, 45-54, 59-68, 72
    src/test_server.py      18      0   100%
    --------------------------------------------------
    TOTAL                   80     31    61%


    =================================== 16 passed in 0.09 seconds ====================================





## Python2 Console Tests:

### Valid methods:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET I eat  éclaires"
    HTTP/1.1 200 OK
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>

-

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET é®ñü®"
    HTTP/1.1 200 OK
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>

-

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET th® blerg woot"
    HTTP/1.1 200 OK
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>

-

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET thñ blerg woot"
    HTTP/1.1 200 OK
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>

-

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET th® blerg woot"
    HTTP/1.1 200 OK
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>

### Invalid methods:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "Get é®ñü®"
    HTTP/1.1 500 Internal Server Error
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Internal Server Error</h1>
    </body>
    </html>

-

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "Get I eat  éclaires"
    HTTP/1.1 500 Internal Server Error
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Internal Server Error</h1>
    </body>
    </html>

-

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "Get th® blerg woot"
    HTTP/1.1 500 Internal Server Error
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Internal Server Error</h1>
    </body>
    </html>

-

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "Get thñ blerg woot"
    HTTP/1.1 500 Internal Server Error
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Internal Server Error</h1>
    </body>
    </html>

-

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "Get thü blerg woot"
    HTTP/1.1 500 Internal Server Error
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Internal Server Error</h1>
    </body>
    </html>

-

    (env) Williams-MacBook-Pro:src ben$ "Get th® blerg woot"
    -bash: Get th® blerg woot: command not found
    (env) Williams-MacBook-Pro:src ben$ python2 client.py "Get th® blerg woot"
    HTTP/1.1 500 Internal Server Error
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Internal Server Error</h1>
    </body>
    </html>

