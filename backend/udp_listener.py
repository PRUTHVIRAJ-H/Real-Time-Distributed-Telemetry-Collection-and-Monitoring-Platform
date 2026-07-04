import socket
from node_registry import update_node

from pprint import pprint 
from node_registry import nodes

UDP_IP = "0.0.0.0"
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on UDP port {UDP_PORT}...")

while True:
    data, addr = sock.recvfrom(1024)
    device_id, seq, value = data.decode().split(',')

    node = update_node(
        device_id,
        int(seq),
        float(value),
        addr[0]
    )

    pprint(node)