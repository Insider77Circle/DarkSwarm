"""MockRuntime — minimal safe fallback runtime for testing and default operation."""

import time
import uuid


class MockRuntime:
    """Mock runtime that simulates inference. No real model needed."""

    def __init__(self):
        self.loaded = False
        self.model_path = None

    def load(self, model_path: str, quantization: str = "auto") -> bool:
        self.model_path = model_path
        self.loaded = True
        return True

    def unload(self) -> bool:
        self.loaded = False
        return True

    def infer(self, prompt: str, max_tokens: int = 512, temperature: float = 0.7) -> dict:
        time.sleep(0.05)  # Simulate minimal latency
        return {
            "text": f"[MockRuntime] Echo: {prompt[:50]}...",
            "tokens_per_sec": 100.0,
            "energy_cost": 0.01,
        }

    def detect_hardware(self) -> dict:
        return {"gpu": None, "vram_gb": 0, "ram_gb": 8.0, "tier": "edge"}

    def detect_models(self) -> list:
        return [{"path": "mock", "type": "mock", "quant": "q4"}]