# Runtime Plugin System

DarkSwarm uses a plugin-based model runtime architecture. This allows different inference backends to be swapped without changing the core node code.

## Architecture

```
DarkSwarmNode
    │
    ├── runtime_registry.py  ← Plugin registry (discovery + resolution)
    │
    ├── backends/
    │   ├── mock_runtime.py  ← MockRuntime (default fallback)
    │   └── llama_runtime.py ← LlamaRuntime (optional, requires llama-cpp-python)
    │
    └── interfaces/
        └── model_runtime.py ← Abstract interface
```

## How It Works

1. **DarkSwarmNode** accepts an optional `model_runtime` parameter (Dependency Injection).
2. If no runtime is injected, the node calls `discover_entry_points()` then `resolve_runtime()`.
3. Resolution checks: config `runtime` key → `DARKSWARM_RUNTIME` env var → falls back to MockRuntime.
4. The resolved runtime is used for all inference operations.

## Registering a Backend

### Via setuptools entry_points

Add to your `setup.py`:

```python
entry_points={
    "darkswarm.model_runtimes": [
        "my_runtime = mypackage.mymodule:MyRuntime",
    ],
}
```

### Via code

```python
from node.runtime_registry import register_runtime
from mypackage import MyRuntime

register_runtime("my_runtime", MyRuntime)
```

## Environment Variables

| Variable | Description |
|---|---|
| `DARKSWARM_RUNTIME` | Name of the runtime to use (e.g., "llama", "mock") |

## Built-in Runtimes

| Name | Class | Requires |
|---|---|---|
| `mock` | `MockRuntime` | None (always available) |
| `llama` | `LlamaRuntime` | `llama-cpp-python` |