# http-server

An http server using python sockets.

## Tox:

    platform darwin -- Python 3.5.2, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
    rootdir: /Users/ben/401/http-server2/http-server, inifile: 
    plugins: cov-2.4.0
    collected 4 items 

    src/test_server.py ....

    ---------- coverage: platform darwin, python 3.5.2-final-0 -----------
    Name                 Stmts   Miss  Cover   Missing
    --------------------------------------------------
    src/client.py           22      2    91%   11, 30
    src/server.py           38     29    24%   11-35, 45-54, 59-68, 72
    src/test_server.py      15      0   100%
    --------------------------------------------------
    TOTAL                   75     31    59%


    ============================= 4 passed in 0.06 seconds =============================
    
-

    platform darwin -- Python 2.7.13, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
    rootdir: /Users/ben/401/http-server2/http-server, inifile: 
    plugins: cov-2.4.0
    collected 4 items 

    src/test_server.py ....

    ---------- coverage: platform darwin, python 2.7.13-final-0 ----------
    Name                 Stmts   Miss  Cover   Missing
    --------------------------------------------------
    src/client.py           22      2    91%   11, 30
    src/server.py           38     29    24%   11-35, 45-54, 59-68, 72
    src/test_server.py      15      0   100%
    --------------------------------------------------
    TOTAL                   75     31    59%


    ============================= 4 passed in 0.05 seconds =============================





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
