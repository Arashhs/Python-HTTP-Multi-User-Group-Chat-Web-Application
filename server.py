#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import random, string


HOST_NAME='localhost'
PORT_NUMBER=8000
TOKEN_LENGTH=12

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class MainHandler(BaseHTTPRequestHandler):
    users = {}

    def do_GET(self):
        self.send_response(200)
        self.send_header("username", "123dszfasdf")
        self.end_headers()
    #    self.wfile.write()

    def do_POST(self):
        users = self.users
        length = int(self.headers['content-length'])
        body = self.rfile.read(length).decode('utf-8')
        print(body)
        self.send_response(200)
        self.end_headers()
        # self.wfile.write("Received POST request with body: " + body)
        if(self.path == '\join'):
            token = id_generator(TOKEN_LENGTH)
            # print(token)
            self.wfile.write(token.encode('utf-8'))
            users[token] = body
            print('User {} joined the chat.'.format(body))
            print(users)
        elif(self.path == "\quit"):
            print('User {} left the chat.'.format(users[self.headers['token']]))
            users.pop(self.headers['token'], None)
            print(users)
        else:
            messageBody = body
            sender = users[self.headers['token']]
            sendMessage = {'sender':sender, 'body':messageBody}
            print(sendMessage)









def main():
    print("Server is running: {}:{}".format(HOST_NAME, PORT_NUMBER))
    server = HTTPServer(("0.0.0.0", 8000), MainHandler)
    server.serve_forever()



if __name__ == '__main__':
    main()
    