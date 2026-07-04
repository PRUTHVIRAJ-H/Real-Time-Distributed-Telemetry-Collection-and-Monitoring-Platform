from datetime import datetime

nodes = {}


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
            "packets_received": 1
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

    node["history"].append(value)

    if len(node["history"]) > 20:
        node["history"].pop(0)

    return node