# this is server for the lab1
# import socket module
import sys
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 80
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('the web server is up on port:', serverPort)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        print(message, '::', message.split()[0], ':', message.split()[1])
        filename = message.split()[1]
        print('\n', filename, '||', filename[1:], '\n')
        f = open(filename[1:])
        outputData = f.read()
        print(outputData)
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\n\n'.encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())

    connectionSocket.close()
    serverSocket.close()
    sys.exit()
