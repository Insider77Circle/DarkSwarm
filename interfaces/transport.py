"""Transport Interface — Node-to-node communication."""

class Transport:
    """Abstract interface for network transport backends."""

    def start(self, listen_addrs: list) -> bool:
        """Start listening on given addresses. Returns True on success."""
        ...

    def stop(self) -> bool:
        """Stop the transport layer."""
        ...

    def connect(self, peer_id: str, addr: str) -> bool:
        """Connect to a peer."""
        ...

    def disconnect(self, peer_id: str) -> bool:
        """Disconnect from a peer."""
        ...

    def send_message(self, peer_id: str, message: bytes) -> bool:
        """Send a message to a connected peer."""
        ...

    def broadcast(self, message: bytes, topic: str) -> bool:
        """Broadcast a message on a pubsub topic."""
        ...

    def discover_peers(self, topic: str) -> list:
        """Discover peers on a pubsub topic."""
        ...

    def get_connected_peers(self) -> list:
        """Get list of currently connected peers."""
        ...