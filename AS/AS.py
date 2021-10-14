import requests 
import socket
import json

serverPort   = 53533

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', serverPort))

while True:
    print ('Waiting to listen')
    response, clientaddress = s.recvfrom(2048)
    response = response.decode()
    response = json.loads(response)

    if len(response) == 4:
        db = {response["NAME"]: response}  ##dictionary
        as_object = json.dumps(db)
        with open("out.json", "w") as outfile:
            outfile.write(as_object)
        s.sendto(str(201).encode(), clientaddress)

    else:
         with open("out.json", "r") as outfile:
            dictionary = json.load(outfile)
        DNS_response = dictionary[response["NAME"]]
        dns_object = json.dumps(DNS_response)
        s.sendto(dns_object.encode(),clientaddress)
        
