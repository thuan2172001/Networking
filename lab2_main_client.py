from socket import *

client_socket = socket(AF_INET, SOCK_DGRAM)
server_addr = ('112.137.129.129', 27001)

try:
    # message = {
    #     "type": 0,
    #     "len": 8,
    #     "data": "12345678",
    # }
    # messageToSend = "".join("%s:%s" % (item, message[item]) for item in message)
    typeOfPacket = "0"
    lenOfPacket = "8"
    sent = client_socket.sendto(typeOfPacket.encode(), server_addr)
    sent = client_socket.sendto(lenOfPacket.encode(), server_addr)
    sent = client_socket.sendto("12345678".encode(), server_addr)
    # print("Sent: \n" + messageToSend)
    data, server = client_socket.recvfrom(1024)
    print("Received: " + data.decode())
finally:
    client_socket.close()
