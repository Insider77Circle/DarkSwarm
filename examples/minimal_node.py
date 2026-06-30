"""Minimal DarkSwarm node - 15 lines."""
from node.darkswarm_node import DarkSwarmNode

node = DarkSwarmNode()
node.start()
try:
    while True:
        import time
        time.sleep(1)
except KeyboardInterrupt:
    node.stop()