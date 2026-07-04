from datetime import datetime

nodes = {}

#FOR UPDATING NODE INFORMATION
def update_node(device_id, seq, value, ip):
    if device_id not in nodes:
        nodes[device_id] = {
            "device_id": device_id,
            "ip": ip,
            "current_value": value,
            "last_seq": seq,
            "last_seen": datetime.now(),
            "history": [],
            "packet_loss": 0,
            "packets_received": 1,
            "status": "ONLINE"
        }
        return nodes[device_id]

    node = nodes[device_id]
   
    node["packets_received"] += 1

    node["current_value"] = value

    expected = node["last_seq"] + 1

    lost = 0
    if seq > expected:
        lost = seq - expected
    node["packet_loss"] += lost

    node["last_seq"] = seq
    node["last_seen"] = datetime.now()
    node["status"] = "ONLINE"

    node["history"].append(value)

    if len(node["history"]) > 20:
        node["history"].pop(0)

    return node


#FOR CHECKING WHETHER THE DEVICE IS ONLINE OR OFFLINE BASED ON LAST SEEN TIME
OFFLINE_THRESHOLD = 10  # seconds


def update_node_status():
    now = datetime.now()

    for node in nodes.values():
        elapsed = (now - node["last_seen"]).total_seconds()

        if elapsed > OFFLINE_THRESHOLD:
            node["status"] = "OFFLINE"
        else:
            node["status"] = "ONLINE"