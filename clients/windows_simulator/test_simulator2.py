import socket
import random
import threading
import time

SERVER_IP = "127.0.0.1"
SERVER_PORT = 4210


def client(device_id):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    seq = 0

    while True:
        seq += 2

        value = random.randint(20, 100)

        message = f"{device_id},{seq},{value}"

        sock.sendto(
            message.encode(),
            (SERVER_IP, SERVER_PORT)
        )

        print("Sent:", message)

        time.sleep(1)


c = 60
while c > 0:
    time.sleep(1)
    client("Test1")
    c-=1

