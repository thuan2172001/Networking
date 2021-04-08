from socket import *
import time
import random

received_host = 'localhost'
received_port = 12000

remote_host = 'localhost'
remote_port = 8000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((received_host, received_port))

simulate_packet_loss = True
sleep_for_rand_response_times = True

sequence_number = 0
received_time = 0


def get_time():
    return int(round(time.time() * 1000))


def send_message(msg, wait=False):
    serverSocket.sendto(msg, (remote_host, remote_port))
    if not wait:
        return


while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    print(get_time() - received_time)
    if received_time != 0 and get_time() - received_time > 5000:
        print('Client disconnect (timeout)')
        sequence_number = 0
        received_time = 0

    message = message.decode().upper()
    received_size = len(message)
    received_array = message.split(' ')
    received_type = received_array[0].upper()
    # print received_type
    received_seq = int(received_array[1])
    received_time = int(received_array[2])
    if received_seq != sequence_number + 1:
        if sequence_number != 0:
            for i in range(sequence_number, received_seq):
                print('Dropped Packet:' + str(i))
        if sequence_number == 0:
            print('Client connect.')
        sequence_number = received_seq
    print('Receive: ' + message)
    # If rand is less is than 4, we consider the packet lost and do not respond
    if sleep_for_rand_response_times:
        min_sleep = 0.2
        max_sleep = 1.0
        time.sleep(random.uniform(min_sleep, max_sleep))
        if simulate_packet_loss:
            if random.randint(0, 10) < 2:
                print('Dropped, lol')
                continue
    elif simulate_packet_loss:
        if random.randint(0, 10) < 4:
            print('Dropped, lol')
            continue
    serverSocket.sendto(message.encode(), address)
    print('Send: ' + message)
