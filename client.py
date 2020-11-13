#!/usr/bin/env python3
import http.client
import atexit


HOST_NAME='localhost'
PORT_NUMBER=8000
token=""
conn=None
headers={}


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
    while True:
        message = input()
        conn.request("POST", "", message, headers=headers)
        response = conn.getresponse()



def exit_handler():
    global headers
    conn.request("POST", "\quit", headers=headers)
    print('My application is ending!')



if __name__ == '__main__':
    main()
    