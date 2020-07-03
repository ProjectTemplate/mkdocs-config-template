import json
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

auth_key = ""
lock = threading.Lock()


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "    access path: " + self.path)
        if auth_key in self.path:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "    auth success: " + self.path)
            t = threading.Thread(target=rebuild)
            t.start()
            self.wfile.write(json.dumps('run rebuild').encode())
        else:
            self.wfile.write(json.dumps('auth failed').encode())
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "    auth failed: " + self.path)


def rebuild():
    if lock.acquire(blocking=False):
        try:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "    rebuild start ...")
            result = os.popen("sh build.sh")
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "    run rebuild result: " + result.read())
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "    rebuild end ...")
        finally:
            lock.release()
    else:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "rebuild is running skip")


if __name__ == '__main__':
    bind_host = sys.argv[1]
    bind_port = int(sys.argv[2])
    auth_key = sys.argv[3]

    server_address = ('127.0.0.1', bind_port)

    httpd = HTTPServer((bind_host, bind_port), Server)
    httpd.serve_forever()
