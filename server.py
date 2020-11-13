#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import random, string


HOST_NAME='localhost'
PORT_NUMBER=8000
TOKEN_LENGTH=12

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class MainHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("username", "123dszfasdf")
        self.end_headers()
    #    self.wfile.write()

    def do_POST(self):
        length = int(self.headers['content-length'])
        body = self.rfile.read(length)
        self.send_response(200)
        self.end_headers()
        # self.wfile.write("Received POST request with body: " + body)
        if(self.path == '\join'):
            token = id_generator(TOKEN_LENGTH)
            print(token)
            self.wfile.write(b'token')






def main():
    print("Server: {}:{}".format(HOST_NAME, PORT_NUMBER))
    server = HTTPServer(("0.0.0.0", 8000), MainHandler)
    server.serve_forever()



if __name__ == '__main__':
    main()
    