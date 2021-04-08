from socket import *
import time
import random

receive_host = 'localhost'
receive_port = 8000

remote_host = 'localhost'
remote_port = 12000

# number of times to ping
num_pings = 10

# Keep track of some things
sequence_number = 1
min_rtt = 0
max_rtt = 0
avg_rtt = 0
packets_dropped = 0.0
total_packets = 0.0

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.settimeout(1.0)
serverSocket.bind((receive_host, receive_port))


def get_time():
    return int(round(time.time() * 1000))


def wait_for_response():
    global packets_dropped
    while True:
        # Generate random number in the range of 0 to 10 rand = random.randint(0, 10)
        # Receive the client packet along with the address it is coming from
        try:
            msg, address = serverSocket.recvfrom(1024)
            return msg.decode()
        except Exception:
            packets_dropped = packets_dropped + 1
            return 'ERROR 522 ' + str(get_time()) + ' TIMEOUT'


def send_message(msg, wait=False):
    serverSocket.sendto(msg.encode(), (remote_host, remote_port))
    if not wait:
        return
    else:
        return wait_for_response()


while True:
    time.sleep(1)
    if random.randint(0, 10) < 4:
        sequence_number = sequence_number + 1
        print('Dropped, lol')
        continue
    # Create message with current sequence_number and time
    message = 'PING ' + str(sequence_number) + ' ' + str(get_time())
    # receive ping
    received = send_message(message, True)
    received_size = len(received)
    received_array = received.split(' ')
    received_type = received_array[0].upper()
    received_seq = received_array[1]
    received_time = int(received_array[2])
    rtt = get_time() - received_time
    if rtt > 1000:
        continue
    if received_type == 'PING':
        print(str(received_size) + " bytes received from " + remote_host + ':'
              + str(remote_port) + ': seq=' + str(received_seq) + ' rtt=' + str(rtt))
        avg_rtt = avg_rtt + rtt
        if rtt < min_rtt or min_rtt == 0:
            min_rtt = rtt
        if rtt > max_rtt or max_rtt == 0:
            max_rtt = rtt
        sequence_number = sequence_number + 1
    elif received_type == 'ERROR':
        received_message = received_array[3]
        print(received)
        if received_message == 'TIMEOUT':
            sequence_number = 1
            print('Timeout: waiting 5 seconds before reconnect')
            time.sleep(5)
    else:
        print('Something went wrong, but I have no idea what it is.')
    last = received

    total_packets = total_packets + 1
# Out of the loop, report running statistics
print("RTT: min=" + str(min_rtt) + " max=" + str(max_rtt) + " avg=" + str(avg_rtt/10))
print("Packet Loss: " + str(packets_dropped/total_packets*100) + "%")
