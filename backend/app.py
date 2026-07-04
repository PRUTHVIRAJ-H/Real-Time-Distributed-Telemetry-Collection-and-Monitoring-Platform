from flask import Flask, jsonify
from flask_cors import CORS
from models.node_registry import nodes
from services.udp_listener import start_udp_listener
from services.status_monitor import start_status_monitor
import threading

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return {
        "message": "FleetPulse API Running"
    }


@app.route("/api/nodes")
def get_nodes():
    result = []

    for node in nodes.values():
        n = node.copy()

        if "last_seen" in n:
            n["last_seen"] = n["last_seen"].isoformat()

        if "first_seen" in n:
            n["first_seen"] = n["first_seen"].isoformat()

        result.append(n)

    return jsonify(result)


@app.route("/api/nodes/<device_id>")
def get_node(device_id):
    if device_id not in nodes:
        return jsonify({"error": "Device not found"}), 404

    n = nodes[device_id].copy()

    if "last_seen" in n:
        n["last_seen"] = n["last_seen"].isoformat()

    if "first_seen" in n:
        n["first_seen"] = n["first_seen"].isoformat()

    return jsonify(n)


@app.route("/api/history/<device_id>")
def get_history(device_id):
    if device_id not in nodes:
        return jsonify([])

    history = nodes[device_id]["history"]

    result = [
        {
            "time": i,
            "value": v
        }
        for i, v in enumerate(history)
    ]

    return jsonify(result)


if __name__ == "__main__":
    threading.Thread(
        target=start_udp_listener,
        daemon=True
    ).start()

    threading.Thread(
        target=start_status_monitor,
        daemon=True
    ).start()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )