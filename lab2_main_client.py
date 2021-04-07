import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12000)
sock.settimeout(1.0)
min_rtt = 0
max_rtt = 0
rtt_receive_size = 0
rtt_sum = 0

try:
    for i in range(1, 11):
        start = time.time()
        message = 'Ping #' + str(i) + " " + time.ctime(start)
        try:
            sent = sock.sendto(message.encode(), server_addr)
            print("Sent: " + message)
            data, server = sock.recvfrom(4096)
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
        except socket.timeout:
            print("#" + str(i) + " Requested Time out\n")

finally:
    print("Min rtt is: " + str(min_rtt))
    print("Max rtt is: " + str(max_rtt))
    print("Average rtt is: " + str(rtt_sum / rtt_receive_size))
    print("Packet lost rate is: " + str((1 - rtt_receive_size / 10) * 100) + "%")
    print("closing socket")
    sock.close()
