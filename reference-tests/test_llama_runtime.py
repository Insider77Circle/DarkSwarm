"""Tests for LlamaRuntime (uses mocking to avoid real model dependency)."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from node.backends.llama_runtime import LlamaRuntime, HAS_LLAMA


def test_llama_runtime_importable():
    """LlamaRuntime class should be importable regardless of llama-cpp-python."""
    assert LlamaRuntime is not None


def test_llama_runtime_fallback_on_missing():
    """If llama-cpp-python is not installed, load() returns False."""
    runtime = LlamaRuntime()
    result = runtime.load("/fake/path")
    if not HAS_LLAMA:
        assert result is False
    # If llama IS installed, this may still fail due to missing model, but shouldn't crash


def test_llama_runtime_infer_empty():
    """Infer with no loaded model returns empty result."""
    runtime = LlamaRuntime()
    result = runtime.infer("test")
    assert result["text"] == ""
    assert result["tokens_per_sec"] == 0.0


def test_llama_runtime_unload():
    runtime = LlamaRuntime()
    assert runtime.unload() is True


def test_llama_runtime_detect_hardware():
    runtime = LlamaRuntime()
    info = runtime.detect_hardware()
    assert "tier" in info


if __name__ == "__main__":
    test_llama_runtime_importable()
    test_llama_runtime_fallback_on_missing()
    test_llama_runtime_infer_empty()
    test_llama_runtime_unload()
    test_llama_runtime_detect_hardware()
    print("All LlamaRuntime tests passed.")