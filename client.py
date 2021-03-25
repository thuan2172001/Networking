# this is client for the lab1-optional exercises

from socket import *
import sys

"""
Command line: client.py server_host server_port filename
"""
server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

host_port = "%s:%s" % (server_host, server_port)
try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_host, int(server_port)))
    header = {
        "first_header": "GET /%s HTTP/1.1" % filename,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Host": host_port,
    }
    http_header = "\n".join("%s:%s" % (item, header[item]) for item in header)
    print(http_header)
    client_socket.send(("%s" % http_header).encode())
except IOError:
    sys.exit(1)

final = ""
response_message = client_socket.recv(1024)
while response_message:
    final += response_message.decode()
    response_message = client_socket.recv(1024)

client_socket.close()
print("\nfinal: ", final)
