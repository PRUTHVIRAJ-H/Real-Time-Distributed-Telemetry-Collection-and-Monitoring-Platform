import socket

from node_registry import (
    update_node,  # To update the nodes
    update_node_status, # To check whetehr the device is online or offline based on last seen time
    nodes # Just all the nodes 
)

import threading
import time

from pprint import pprint 


UDP_IP = "0.0.0.0"
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on UDP port {UDP_PORT}...")


threading.Thread(
    target=status_monitor,
    daemon=True
).start()

# FOR CONCURRENCY 
#      1 THREAD -> HANDLING SOCKETS
#      2 THREAD -> HANDLING UPDATING NODE STATUS



# THREAD 1

while True:
    data, addr = sock.recvfrom(1024)
    device_id, seq, value = data.decode().split(',')

    # UPDATING NODE VALUE
    node = update_node(
        device_id,
        int(seq),
        float(value),
        addr[0]
    )

    # UPDATING NODE ONLINE OR OFFLINE STATUS
    update_node_status()



# THREAD 2

def status_monitor():
    while True:
        update_node_status()
        time.sleep(1)
