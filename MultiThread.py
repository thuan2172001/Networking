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
                message = connectionSocket.recv(1024)
                # Fill in start #Fill in end
                if not message:
                    break
                print("message: \n", message)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
                print("outputdata:", outputdata)
                now = datetime.datetime.now()
                # Fill in start #Fill in end
                # Send one HTTP header line into socket
                # Fill in start

                first_header = "HTTP/1.1 200 OK"
                # alive ={
                # 	"timeout":10,
                # 	"max":100,
                # }
                header_info = {
                    "Date": now.strftime("%Y-%m-%d %H:%M"),
                    "Content-Length": len(outputdata),
                    "Keep-Alive": "timeout=%d,max=%d" % (10, 100),
                    "Connection": "Keep-Alive",
                    "Content-Type": "text/html"
                }

                following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
                print("following_header:", following_header)
                connectionSocket.send(("%s\r\n%s\r\n\r\n" % (first_header, following_header)).encode())

                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
            except IOError:
                connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())


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

    # main thread wait all threads finish then close the connection
