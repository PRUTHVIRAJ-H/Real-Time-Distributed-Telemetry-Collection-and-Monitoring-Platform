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
        seq += 1

        value = random.randint(20, 100)

        message = f"{device_id},{seq},{value}"

        sock.sendto(
            message.encode(),
            (SERVER_IP, SERVER_PORT)
        )

        print("Sent:", message)

        time.sleep(1)


for i in range(5):
    threading.Thread(
        target=client,
        args=(f"SIM_{i}",),
        daemon=True
    ).start()

while True:
    time.sleep(1)