"""Storage Interface — Persistent state and model weights."""

class Storage:
    """Abstract interface for storage backends."""

    def store(self, key: str, value: bytes) -> bool:
        """Store a value. Returns True on success."""
        ...

    def retrieve(self, key: str) -> bytes:
        """Retrieve a value by key."""
        ...

    def store_model(self, model_name: str, model_path: str) -> bool:
        """Store model weights for P2P distribution."""
        ...

    def retrieve_model(self, model_name: str, destination: str) -> bool:
        """Download model weights from swarm."""
        ...

    def pin(self, cid: str) -> bool:
        """Pin content to local storage (IPFS pin)."""
        ...

    def list_local_models(self) -> list:
        """List models available on this node."""
        ...

    def get_usage_stats(self) -> dict:
        """Get storage usage statistics."""
        ...