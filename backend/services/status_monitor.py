import time
from node_registry import update_node_status


def start_status_monitor():
    while True:
        update_node_status()
        time.sleep(1)