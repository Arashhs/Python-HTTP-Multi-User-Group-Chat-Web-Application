#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import random, string, threading
from socketserver import ThreadingMixIn
import json, time



HOST_NAME='localhost'
PORT_NUMBER=8000
TOKEN_LENGTH=12
messageQueue = {}
num = 0
lock = threading.Lock()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class MainHandler(BaseHTTPRequestHandler):
    users = {}
    getThreads = {}
    global messageQueue
    global num

    def getResp(self):
        global messageQueue
        global num

        """     while True:
            with lock:
                userName = self.users[self.headers['token']]
                if(num != 0):
                    print("receiver is: {} | Message is: {}".format(userName, messageQueue))
                    self.send_response(200)
                    self.end_headers()
                    jsMes = json.dumps(messageQueue)
                    self.wfile.write(jsMes.encode(encoding='utf-8'))
                    num -= 1
                    break 
        """
        while True:
            with lock:
                mes = messageQueue
            userName = self.users[self.headers['token']]
            if(num != 0):
                print("receiver is: {} | Message is: {}".format(userName, mes))
                self.send_response(200)
                self.end_headers()
                jsMes = json.dumps(mes)
                self.wfile.write(jsMes.encode(encoding='utf-8'))
                num -= 1
                break

    def do_GET(self):
        # self.send_response(200)
        # self.send_header("username", "123dszfasdf")
        # self.end_headers()
        # self.wfile.write("hello Bak".encode('utf-8'))
        # getThread = threading.Thread(target=self.getResp, args=self)
        # getThread.daemon = True
        # getThread.start()
        self.getResp()

    def do_POST(self):
        global num
        global messageQueue 
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
            while True:
                with lock:
                    if(num==0):
                        break

            messageBody = body
            sender = users[self.headers['token']]
            sendMessage = {'sender':sender, 'body':messageBody}
            print(sendMessage)
            num += len(users)
            messageQueue = sendMessage

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""




def main():
    print("Server is running: {}:{}".format(HOST_NAME, PORT_NUMBER))
    server = ThreadedHTTPServer(("0.0.0.0", 8000), MainHandler)
    server.serve_forever()



if __name__ == '__main__':
    main()
    