import requests
import socket
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/fibonacci')
def Fibonacci(n):

	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	elif n < 0:
		return('Invalid input')
	else:
		return Fibonacci(n - 1) + Fibonacci(n - 2)

def top_program():
	num = request.args.get('number')
	n=int(num)
	result = Fibonacci(n)
	return str(result)

@app.route('/register')
def Register():
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    dictionary = {
	"hostname": request.args.get('hostname'),
	"ip": request.args.get('ip'),
	"as_ip" : request.args.get('as_ip'),
	"as_port" : request.args.get('as_port')
	}
    out_dictionary = {
    "TYPE": "A",
    "NAME": dictionary["hostname"],
	"VALUE": dictionary["ip"],
    "TTL": 10
    }


    json_object = json.dumps(out_dictionary)
    s.sendto(fs_object.encode(), (dictionar["as_ip"], int(dictionary["as_port"])))
    response, clientaddress = serversocket.recvfrom(2048)
if code == '201':
        return str(201)
    else:
        return ('Error')


app.run(host='0.0.0.0',
        port=9090,
        debug=True)