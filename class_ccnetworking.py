import requests
import sys
import class_json


class Ccnetworking:
    def __init__(self, port, ip, url):
        self._port = port
        self._ip = ip
        self._url = url

    def __get_server_response(self, headers, data):
        response = requests.post(self._url, data=data, headers=headers)

        if response.status_code == 200:
            print("ok response code", response.status_code)

        elif response.status_code == 404:
            print("not found!", response.status_code)
            sys.exit()

        elif response.status_code == 418:
            print("I'm a teapot", response.status_code)
            sys.exit()

        elif response.status_code == 500:
            print("Internal error", response.status_code)
            sys.exit()

        elif response.status_code == 501:
            print("not Implemented", response.status_code)
            sys.exit()

        return response.content

    def get_peers_ip(self, data):
        headers = {'content-type': 'application/json'}
        res = class_json.decodejson(self.__get_server_response(headers, data))

        if isinstance(res['peernodes'], list) and len(res['peernodes']) > 0:
            ip, port = ((res['peernodes'][0]).split(':'))

            return ip, port
        else:
            print('serverresponse was empty')
            sys.exit()
            return None

