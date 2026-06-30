"""TaskType Interface — Define executable task schemas."""

class TaskType:
    """Abstract interface for task type definitions."""

    def register(self, task_type: str, schema: dict) -> bool:
        """Register a new task type with its schema."""
        ...

    def validate(self, task: dict) -> bool:
        """Validate a task against its type schema."""
        ...

    def serialize(self, task: dict) -> bytes:
        """Serialize a task to wire format."""
        ...

    def deserialize(self, data: bytes) -> dict:
        """Deserialize a task from wire format."""
        ...


# Built-in task types
TASK_TYPES = {
    "text_generation": {
        "prompt": "string",
        "max_tokens": "int",
        "temperature": "float",
        "model_preference": "string (optional)"
    },
    "code_generation": {
        "prompt": "string",
        "language": "string",
        "max_tokens": "int"
    },
    "analysis": {
        "content": "string",
        "task_type": "string (summarize|critique|classify|extract)"
    },
    "agent_chain": {
        "steps": "list",
        "context": "string",
        "max_rounds": "int"
    },
    "adversarial_probe": {
        "probe_type": "string",
        "target_model": "string",
        "expected_behavior": "string"
    }
}