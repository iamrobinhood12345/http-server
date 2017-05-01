# http-server

An http server using python sockets.

## Tox:

        platform darwin -- Python 3.5.2, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
        rootdir: /Users/ben/401/http-server2/http-server, inifile: 
        plugins: cov-2.4.0
        collected 31 items 

        src/test_server.py ...............................

        ---------- coverage: platform darwin, python 3.5.2-final-0 -----------
        Name                 Stmts   Miss  Cover   Missing
        --------------------------------------------------
        src/client.py           27      4    85%   18-19, 26, 37
        src/server.py           87     44    49%   10-23, 28-34, 47-49, 75, 80, 88, 94-111, 163, 177
        src/test_server.py      60      0   100%
        --------------------------------------------------
        TOTAL                  174     48    72%


        ========================== 31 passed in 0.17 seconds ===========================

  
-

        platform darwin -- Python 2.7.13, pytest-3.0.6, py-1.4.32, pluggy-0.4.0
        rootdir: /Users/ben/401/http-server2/http-server, inifile: 
        plugins: cov-2.4.0
        collected 31 items 

        src/test_server.py ...............................

        ---------- coverage: platform darwin, python 2.7.13-final-0 ----------
        Name                 Stmts   Miss  Cover   Missing
        --------------------------------------------------
        src/client.py           27      3    89%   21, 28, 37
        src/server.py           87     44    49%   10-23, 28-34, 47-49, 75, 80, 88, 94-111, 163, 177
        src/test_server.py      60      0   100%
        --------------------------------------------------
        TOTAL                  174     47    73%


        ========================== 31 passed in 0.14 seconds ===========================
    
