#!/usr/bin/env python3
import http.client
import atexit
import threading, json

HOST_NAME='localhost'
PORT_NUMBER=8000
TIMEOUT = 10000
token=""
conn=None
headers={}


def recMessages(userName):
    while True:
        rcon = http.client.HTTPConnection(HOST_NAME, PORT_NUMBER)
        rcon.request("GET", "", headers=headers)
        while True:
            try:
                response = rcon.getresponse()
                recMesJson = response.read().decode('utf-8')
                recMes = json.loads(recMesJson)
                if (recMes['sender'] != userName and recMes != {}):
                    print('{}: {}'.format(recMes['sender'], recMes['body']))
                break
            except:
                pass
        # response = rcon.getresponse()
        # recMes = response.read().decode('utf-8')
        # print(recMes)



def main():
    global conn 
    global token
    global headers

    userName = input('Please Enter Your Name: ')
    conn = http.client.HTTPConnection(HOST_NAME, PORT_NUMBER)
    # conn.request("GET", "/")
    # r1 = conn.getresponse()
    # print(r1.status, r1.reason)
    # data1 = r1.read()  # This will return entire content.
    # The following example demonstrates reading data in chunks.
    # conn.request("GET", "/")
    # r1 = conn.getresponse()
    # print(r1.getheader("username"))
    conn.request("POST", "\join", userName)
    response = conn.getresponse()
    token = response.read().decode('utf-8')
    headers = {'token':token}
    print('You joined the chat. Your auth is: {}'.format(token))
    # print(response.status, response.reason, response.read())
    atexit.register(exit_handler)
    recThread = threading.Thread(target=recMessages, args=(userName,))
    recThread.daemon = True
    recThread.start()
    while True:
        message = input()
        conn.request("POST", "", message, headers=headers)
        response = conn.getresponse()




def exit_handler():
    global headers
    conn.request("POST", "\quit", headers=headers)
    print("You're leving the chat, bye!")



if __name__ == '__main__':
    main()
    