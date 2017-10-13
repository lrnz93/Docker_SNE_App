from class_ccnetworking import Ccnetworking
import class_json
import class_hostip


def main():

    data = class_json.encodejson()
    hostip = (class_hostip.getownip())
    ccserver = Ccnetworking(8091, hostip, 'http://localhost:8091/v1.0/aanmelden/')
    ip, port = ccserver.get_peers_ip(data)
    print(ip)
    print(port)

main()
