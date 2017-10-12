import json

def encodejson():

    data = {"cc": "172.17.0.34:8080", "peernodes": ["172.17.0.32:8079","172.17.0.33:8078"]}
    try:
        json_str = json.dumps(data, separators=(',', ':'))

    except(ValueError, KeyError,TypeError):
        print ("Json error!")

    return json_str;

def decodejson(encodedjson):

    decodedata = json.loads(encodedjson)

    return decodedata;
