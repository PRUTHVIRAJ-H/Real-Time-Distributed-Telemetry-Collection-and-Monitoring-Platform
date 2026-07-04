from flask import Flask, jsonify
from node_registry import nodes
from udp_listener import start_udp_listener
from status_monitor import start_status_monitor
import threading

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "FleetPulse API Running"
    }


@app.route("/api/nodes")
def get_nodes():
    return jsonify(list(nodes.values()))


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
        debug=False
    )