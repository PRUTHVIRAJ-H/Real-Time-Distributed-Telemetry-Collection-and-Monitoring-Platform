import socket
from models.node_registry import update_node
from services.database_service import (
    save_device,
    save_telemetry
)


HOST = "0.0.0.0"
PORT = 4210


def start_udp_listener():
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM
    )

    sock.bind((HOST, PORT))

    print(f"🚀 UDP listening on {PORT}")

    while True:
        data, addr = sock.recvfrom(1024)

        message = data.decode()

        try:
            device_id, seq, value = message.split(',')

            update_node(
                device_id,
                int(seq),
                float(value),
                addr[0]
            )

            save_device(node)
            save_telemetry(
                node["device_id"],
                node["current_value"]
            )
        except Exception as e:
            print("Packet Error:", e)