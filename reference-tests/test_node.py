"""DarkSwarm conformance tests."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from node.darkswarm_node import DarkSwarmNode

def test_node_initializes():
    n = DarkSwarmNode()
    assert n.node_id is not None
    assert n.hardware["tier"] in ("edge", "consumer", "pro", "server")

def test_node_start_stop():
    n = DarkSwarmNode()
    n.start()
    assert n.running == True
    n.stop()
    assert n.running == False

def test_node_status():
    n = DarkSwarmNode()
    status = n.get_status()
    assert "node_id" in status
    assert "hardware" in status

if __name__ == "__main__":
    test_node_initializes()
    test_node_start_stop()
    test_node_status()
    print("All tests passed.")