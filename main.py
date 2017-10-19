from class_ccnetworking import Ccnetworking
import class_json
import class_hostip
from class_peernetworking import *
from flask import Flask, session
from class_runningconfig import RunningConfig


def main():
    data = class_json.encodejson()
    hostip = (class_hostip.getownip())

    ccserver = Ccnetworking(8091, hostip, 'http://localhost:8091/v1.0/aanmelden/')
    ip, port = ccserver.get_peers_ip(data)
    print(ip)
    print(port)

    # Create FLASK Instance
    app = Flask(__name__)

    # Register FLASK routes
    app.add_url_rule('/v1.0/reset/', view_func=DistAPIReset.as_view('rest'), methods=['POST'])
    app.add_url_rule('/v1.0/document-info/', view_func=DistAPIDocInfo.as_view('document-info'), methods=['POST'])

    # Set FLASK session vars
    RunningConfig().set_config('ip', ip)
    RunningConfig().set_config('port', port)

    # Run FLASK listner
    app.run(host='127.0.0.1', debug=True, port=5009)


main()
