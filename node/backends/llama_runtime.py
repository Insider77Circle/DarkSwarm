"""LlamaRuntime — optional inference backend via llama-cpp-python."""

import logging

logger = logging.getLogger(__name__)

try:
    from llama_cpp import Llama
    HAS_LLAMA = True
except ImportError:
    Llama = None
    HAS_LLAMA = False


class LlamaRuntime:
    """Runtime backed by llama.cpp via llama-cpp-python."""

    def __init__(self):
        self._model = None
        self._model_path = None

    def load(self, model_path: str, quantization: str = "auto") -> bool:
        if not HAS_LLAMA:
            logger.warning("llama-cpp-python not installed. Cannot load LlamaRuntime.")
            return False
        try:
            self._model = Llama(model_path=model_path, verbose=False)
            self._model_path = model_path
            return True
        except Exception as e:
            logger.error("Failed to load model %s: %s", model_path, e)
            return False

    def unload(self) -> bool:
        self._model = None
        self._model_path = None
        return True

    def infer(self, prompt: str, max_tokens: int = 512, temperature: float = 0.7) -> dict:
        if not self._model:
            return {"text": "", "tokens_per_sec": 0.0, "energy_cost": 0.0}
        output = self._model(prompt, max_tokens=max_tokens, temperature=temperature)
        return {
            "text": output["choices"][0]["text"],
            "tokens_per_sec": 0.0,
            "energy_cost": 0.0,
        }

    def detect_hardware(self) -> dict:
        return {"gpu": None, "vram_gb": 0, "ram_gb": 8.0, "tier": "edge"}

    def detect_models(self) -> list:
        return []