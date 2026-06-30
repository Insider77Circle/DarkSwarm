"""Minimal ModelRuntime using llama-cpp-python (example).

This implements the ModelRuntime interface defined in interfaces/model_runtime.py.
If llama-cpp-python is not installed, load() will return False so the node can fall
back to other runtimes.
"""

from interfaces.model_runtime import ModelRuntime

class LlamaCppRuntime(ModelRuntime):
    def __init__(self):
        self.model = None
        self.model_path = None

    def load(self, model_path: str, quantization: str = "auto") -> bool:
        try:
            from llama_cpp import Llama
        except Exception:
            # package not installed or import failed
            return False
        try:
            self.model = Llama(model_path=model_path)
            self.model_path = model_path
            return True
        except Exception:
            self.model = None
            self.model_path = None
            return False

    def unload(self) -> bool:
        if self.model:
            # llama-cpp-python does not expose explicit unload API; drop reference
            self.model = None
            self.model_path = None
            return True
        return False

    def infer(self, prompt: str, max_tokens: int = 512, temperature: float = 0.7) -> dict:
        if not self.model:
            raise RuntimeError("model not loaded")
        out = self.model.create(prompt=prompt, max_tokens=max_tokens, temperature=temperature)
        # Normalize output to the expected dict shape
        text = ""
        try:
            text = out.get("choices", [{}])[0].get("text", "")
        except Exception:
            # Some runtimes return different shapes; fall back safely
            text = str(out)
        return {
            "text": text,
            "tokens_per_sec": (out.get("usage", {}).get("tokens_per_second") if isinstance(out.get("usage", {}), dict) else 0.0) or 0.0,
            "energy_cost": 0.0,  # placeholder until energy accounting is implemented
        }

    def detect_hardware(self) -> dict:
        # Simple stub; delegate to node hardware detection when available
        return {"gpu": None, "vram_gb": 0.0, "ram_gb": 0.0, "tier": "consumer"}

    def detect_models(self) -> list:
        return [{"path": self.model_path, "type": "llama", "quant": "unknown"}] if self.model_path else []
