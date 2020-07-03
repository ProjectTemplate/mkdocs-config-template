import os
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

auth_key = ""


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + self.path)
        if auth_key in self.path:
            rebuild()


def rebuild():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "    rebuild start ...")
    result = os.popen("sh build.sh")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "    run rebuild result: " + result.read())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "    rebuild end ...")


if __name__ == '__main__':
    bind_host = sys.argv[1]
    bind_port = int(sys.argv[2])
    auth_key = sys.argv[3]

    server_address = ('127.0.0.1', bind_port)

    httpd = HTTPServer((bind_host, bind_port), Server)
    httpd.serve_forever()
