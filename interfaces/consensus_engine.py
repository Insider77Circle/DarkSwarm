"""ConsensusEngine Interface — Verify outputs across multiple nodes."""

class ConsensusEngine:
    """Abstract interface for output verification."""

    TIERS = {
        "fast": {"nodes": 1, "timeout_ms": 100, "description": "Local speculative decode"},
        "standard": {"nodes": 3, "timeout_ms": 2000, "description": "3-node redundant execution"},
        "deep": {"nodes": 5, "timeout_ms": 5000, "description": "Energy-weighted consensus"},
        "debate": {"nodes": 7, "timeout_ms": 30000, "description": "Multi-agent adversarial debate"}
    }

    def select_tier(self, task: dict) -> str:
        """Select consensus tier based on task criticality."""
        ...

    def submit_for_verification(self, output: dict, tier: str) -> str:
        """Submit an output for verification. Returns a verification_id."""
        ...

    def collect_verdicts(self, verification_id: str) -> dict:
        """Collect verdicts from peer nodes. Returns {'agreed': bool, 'confidence': float, 'verdicts': list}."""
        ...

    def energy_weighted_vote(self, verdicts: list, energy_scores: list) -> dict:
        """Weight votes by node energy budget for Deep tier."""
        ...