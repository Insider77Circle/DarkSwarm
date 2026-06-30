"""Tests for the LlamaCppRuntime wrapper.

These tests don't require the real llama-cpp-python package; they monkeypatch
a minimal in-memory dummy implementation to exercise load/infer/unload.
"""

import sys
import types
from node.backends.llama_runtime import LlamaCppRuntime


def test_llama_runtime_with_mock(monkeypatch):
    # Create a dummy module to stand in for llama_cpp
    class DummyLlama:
        def __init__(self, model_path):
            self.model_path = model_path
        def create(self, prompt, max_tokens, temperature):
            return {"choices": [{"text": "ok"}], "usage": {"tokens_per_second": 100.0}}

    dummy_mod = types.ModuleType("llama_cpp")
    dummy_mod.Llama = DummyLlama
    monkeypatch.setitem(sys.modules, "llama_cpp", dummy_mod)

    rt = LlamaCppRuntime()
    assert rt.load("/fake/model/path") is True
    out = rt.infer("hello", max_tokens=5)
    assert out["text"] == "ok"
    assert out["tokens_per_sec"] == 100.0
    assert rt.unload() is True
