#!/usr/bin/env python3
import http.client

HOST_NAME='localhost'
PORT_NUMBER=8000


def main():
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
    conn.request("POST", "\join")
    response = conn.getresponse()
    print(response.status, response.reason, response.read())


if __name__ == '__main__':
    main()
    