from socket import *
import time

client_socket = socket(AF_INET, SOCK_DGRAM)
server_addr = ('localhost', 11999)
client_socket.settimeout(1.0)

min_rtt = 10.0
max_rtt = 0.0
rtt_receive_size = 0
rtt_sum = 0.0

try:
    for i in range(10):
        start = time.time()
        message = 'Ping #' + str(i + 1) + " " + time.ctime(start)
        try:
            sent = client_socket.sendto(message.encode(), server_addr)
            print("Sent: " + message)
            data, server = client_socket.recvfrom(1024)
            print("Received: " + data.decode())
            end = time.time()
            elapsed = end - start
            rtt_receive_size += 1
            rtt_sum += elapsed
            if min_rtt > elapsed:
                min_rtt = elapsed
            if max_rtt < elapsed:
                max_rtt = elapsed
            print("RTT: " + str(elapsed) + " seconds\n")
        except timeout:
            print("#" + str(i + 1) + " Requested Time out\n")

finally:
    print("Min rtt is: " + str(min_rtt))
    print("Max rtt is: " + str(max_rtt))
    print("Average rtt is: " + str(rtt_sum / rtt_receive_size))
    print("Packet lost rate is: " + str(100 - rtt_receive_size / 10 * 100) + "%")
    print("Closing socket")
    client_socket.close()
