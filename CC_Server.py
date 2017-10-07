import makeJson
import socket
import sys

def connectionmake(port, serverIP, jsonmsg):

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
            #send json string
            c.send(jsonmsg.encode())
            print('Sending json message to client', jsonmsg)
        finally:
            # Close the connection with the client
            c.close()
            print('Close connection from', addr)

    return

IP = ''
PORT = 8090
POST = makeJson.makeJson()

connectionmake(PORT, IP, POST)
