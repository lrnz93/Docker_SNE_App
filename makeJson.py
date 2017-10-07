import json

def makeJson():

    data = {"cc": "172.17.0.33:8080", "peernodes": "172.17.0.33:8080 , 172.17.0.43:8080", }

    json_str = json.dumps(data,separators=(',',':'))

    return json_str;



