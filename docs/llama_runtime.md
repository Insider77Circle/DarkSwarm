# LlamaRuntime Backend

Optional inference backend using llama-cpp-python bindings to llama.cpp.

## Requirements

```bash
pip install llama-cpp-python
```

## Usage

```python
from node.backends.llama_runtime import LlamaRuntime

runtime = LlamaRuntime()
loaded = runtime.load("/path/to/model.gguf")
if loaded:
    result = runtime.infer("Hello, world!")
    print(result["text"])
```

## Notes

- If llama-cpp-python is not installed, `load()` returns `False` and the node falls back to MockRuntime.
- The `LlamaRuntime` class is always importable regardless of whether the dependency is installed.
- Supported model formats: GGUF (via llama.cpp).