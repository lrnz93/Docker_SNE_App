from class_networking import Networking
import class_json


def main():

    data = class_json.encodejson()
    network = Networking(8000, '127.0.0.1', 'http://localhost:8091/v1.0/aanmelden/')
    ip, port = network.get_peers_ip(data)
    print (ip)
    print(port)

main()
