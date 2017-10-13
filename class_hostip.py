import socket

def getownip():
    ownip = (socket.gethostbyname(socket.gethostname()))
    return ownip