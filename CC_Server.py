import json1
import socket
import sys
import requests

def cclistener(port, serverIP,):

    try:
        s = socket.socket()
        print("Socket Created")

    except socket.error as msg:

        print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])

        sys.exit()

    s.bind((serverIP, port))

    print("socket binded to port %s" %(port))

    # put the socket into listening mode. 5 in the queue
    s.listen(5)
    print("socket is listening....")

    # a forever loop until we interrupt it or an error occurs

    while True:

        # Establish connection with client.(c is socket object)
        try:

            c, addr = s.accept()
            print('Got connection from', addr)

        finally:
            # Close the connection with the client
            c.close()
            print('Close connection from', addr)

    return


def ccserverpost(url, data):

    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        print("ok" , response.status_code)

    elif response.status_code == 404:
        print("not found!" , response.status_code)

    elif response.status_code == 418:
        print("I'm a teapot" , response.status_code)

    elif response.status_code == 500:
        print("Internal error" , response.status_code)

    elif response.status_code == 501:
        print("not Implemented" , response.status_code)


    return response.content

jsondata = json1.encodejson()
port = 8091
serverip = '172.17.0.2'
url = 'http://localhost:8091/v1.0/aanmelden/'
postdata = ccserverpost(url,jsondata)
print postdata
