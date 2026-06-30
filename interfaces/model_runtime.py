"""ModelRuntime Interface — Load/unload/infer any open-source LLM."""

class ModelRuntime:
    """Abstract interface for model inference backends."""

    def load(self, model_path: str, quantization: str = "auto") -> bool:
        """Load a model. Returns True on success."""
        ...

    def unload(self) -> bool:
        """Unload the current model. Returns True on success."""
        ...

    def infer(self, prompt: str, max_tokens: int = 512, temperature: float = 0.7) -> dict:
        """Run inference. Returns {'text': str, 'tokens_per_sec': float, 'energy_cost': float}."""
        ...

    def detect_hardware(self) -> dict:
        """Detect available hardware. Returns {'gpu': str, 'vram_gb': float, 'ram_gb': float, 'tier': str}."""
        ...

    def detect_models(self) -> list:
        """Scan system for existing open-source LLMs. Returns list of {'path': str, 'type': str, 'quant': str}."""
        ...