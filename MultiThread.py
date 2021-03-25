# this is the multi thread server for the lab1-optional exercises
# import socket module
from socket import *
import datetime
import threading


class ClientThread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address

    def run(self):
        while True:
            try:
                message = connectionSocket.recv(1024).decode()
                # Fill in start #Fill in end
                if not message:
                    break
                print("message:\n", message)
                filename = message.split()[1]
                f = open(filename[1:])
                outputData = f.read()
                print("outputData:", outputData)
                now = datetime.datetime.now()
                # Fill in start #Fill in end
                # Send one HTTP header line into socket
                # Fill in start

                header_info = {
                    "Date": now.strftime("%Y-%m-%d %H:%M"),
                    "Content-Length": len(outputData),
                    "Keep-Alive": "timeout=%d,max=%d" % (10, 100),
                    "Connection": "Keep-Alive",
                    "Content-Type": "text/html"
                }

                following_header = "\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
                print("following_header:\n", following_header)

                connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

                for i in range(0, len(outputData)):
                    connectionSocket.send(outputData[i].encode())
            except IOError:
                try:
                    connectionSocket.send("HTTP/1.1 404 Not Found\n\n".encode())
                    connectionSocket.send("HTTP/1.1 404 Not Found\n\n".encode())
                except OSError:
                    print("Client is off!")

            # connectionSocket.close()


if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a sever socket
    # Fill in start
    serverPort = 80
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    threads = []
    # Fill in end
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        print("addr:\n", addr)
        # Fill in start
        # Fill in end
        client_thread = ClientThread(connectionSocket, addr)
        client_thread.setDaemon(True)
        client_thread.start()
        threads.append(client_thread)




