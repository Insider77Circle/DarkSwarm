"""RoutingStrategy Interface — Assign tasks to capable peers."""

class RoutingStrategy:
    """Abstract interface for task routing algorithms."""

    def find_peers(self, capability_profile: dict, min_reputation: float = 0.0, max_nodes: int = 5) -> list:
        """Find peers matching capability requirements. Returns list of peer dicts."""
        ...

    def select_optimal(self, candidates: list, task: dict) -> dict:
        """Select the optimal peer from candidates based on load, reputation, energy."""
        ...

    def advertise_capabilities(self, capabilities: dict) -> bool:
        """Advertise this node's capabilities to the DHT."""
        ...

    def update_load_metrics(self, current_load: float, energy_state: float) -> None:
        """Update this node's current load and energy state in the DHT."""
        ...