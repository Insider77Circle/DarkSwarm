"""Tests for the runtime plugin registry."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from node.runtime_registry import register_runtime, get_runtime, list_runtimes, resolve_runtime
from node.backends.mock_runtime import MockRuntime


def test_register_and_get():
    register_runtime("test_mock", MockRuntime)
    cls = get_runtime("test_mock")
    assert cls is MockRuntime


def test_list_runtimes():
    register_runtime("test_list", MockRuntime)
    names = list_runtimes()
    assert "test_list" in names


def test_resolve_none():
    assert resolve_runtime() is None


def test_resolve_by_name():
    register_runtime("resolve_test", MockRuntime)
    cls = resolve_runtime("resolve_test")
    assert cls is MockRuntime


def test_resolve_missing():
    assert resolve_runtime("nonexistent") is None


def test_mock_runtime_infer():
    m = MockRuntime()
    result = m.infer("hello", max_tokens=10)
    assert "text" in result
    assert "tokens_per_sec" in result
    assert "energy_cost" in result


def test_mock_runtime_load_unload():
    m = MockRuntime()
    assert m.load("/fake/path") is True
    assert m.unload() is True


if __name__ == "__main__":
    test_register_and_get()
    test_list_runtimes()
    test_resolve_none()
    test_resolve_by_name()
    test_resolve_missing()
    test_mock_runtime_infer()
    test_mock_runtime_load_unload()
    print("All runtime registry tests passed.")