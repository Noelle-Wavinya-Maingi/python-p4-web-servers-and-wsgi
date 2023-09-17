#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response


@Request.application
def application(request):
    print(f"This web server is running at {request.remote_addr}")
    return Response('A WSGI generate this response!')

if __name__ == '__main__':
    # The method runs a server for a one-page application without complications. It requires a hostname, port and application
    from werkzeug.serving import run_simple
    run_simple(
        hostname = 'localhost',
        port = 5555,
        application = application
    )
