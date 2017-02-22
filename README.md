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

### Valid methods:

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "GET the bl®rg woot"
    HTTP/1.1 200 OK
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>
    (env) Williams-MacBook-Pro:src ben$ python3 client.py "GET the bl®rg woot"
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

    (env) Williams-MacBook-Pro:src ben$ python2 client.py "get the bl®rg woot"
    HTTP/1.1 500 Internal Server Error
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Internal Server Error</h1>
    </body>
    </html>
    (env) Williams-MacBook-Pro:src ben$ python3 client.py "get the bl®rg woot"
    HTTP/1.1 500 Internal Server Error
    Server: Teddy Bear
    Content-Type: text/html
    Connection: Closed

    <html>
    <body>
    <h1>Internal Server Error</h1>
    </body>
    </html>
