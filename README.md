# http-server

An http server using python sockets.

## NOTE!!!

Non ascii characters pass Python2 console tests but do not pass tox! (See section Python2 Console Tests)

## Tox:

    src/test_server.py ................

    ---------- coverage: platform darwin, python 3.5.2-final-0 -----------
    Name                 Stmts   Miss  Cover   Missing
    --------------------------------------------------
    src/client.py           24      3    88%   11, 19, 32
    src/server.py           38     29    24%   11-35, 45-54, 59-68, 72
    src/test_server.py      17      0   100%
    --------------------------------------------------
    TOTAL                   79     32    59%


    =================================== 16 passed in 0.17 seconds ====================================
    
-

    ---------- coverage: platform darwin, python 2.7.13-final-0 ----------
    Name                 Stmts   Miss  Cover   Missing
    --------------------------------------------------
    src/client.py           24     24     0%   4-32
    src/server.py           38     38     0%   2-72
    src/test_server.py      17     17     0%   4-68
    --------------------------------------------------
    TOTAL                   79     79     0%

    ============================================= ERRORS =============================================
    ______________________________ ERROR collecting src/test_server.py _______________________________
    .tox/py27/lib/python2.7/site-packages/_pytest/python.py:418: in _importtestmodule
        mod = self.fspath.pyimport(ensuresyspath=importmode)
    .tox/py27/lib/python2.7/site-packages/py/_path/local.py:662: in pyimport
        __import__(modname)
    E     File "/Users/ben/401/http-server2/http-server/src/test_server.py", line 7
    E   SyntaxError: Non-ASCII character '\xc2' in file /Users/ben/401/http-server2/http-server/src/test_server.py on line 7, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
    !!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!





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

