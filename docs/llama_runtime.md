# Llama Runtime Backend

This document explains the minimal LlamaCppRuntime implementation added to node/backends/llama_runtime.py.

Purpose
- Provide a concrete ModelRuntime implementation that wraps llama-cpp-python when available.
- Allow the reference node to run real inference backends once the native dependencies are installed.

Usage
1. Install (optional) llama-cpp-python and a compatible model:

```bash
pip install "llama-cpp-python>=0.1"
# follow llama-cpp-python docs to obtain or convert a model and point to its path
```

2. Use the runtime programmatically:

```python
from node.backends.llama_runtime import LlamaCppRuntime
rt = LlamaCppRuntime()
if rt.load('/path/to/model'):
    res = rt.infer('Hello world', max_tokens=32)
    print(res['text'])
    rt.unload()
else:
    print('llama-cpp-python not available or model failed to load')
```

Notes
- This implementation is intentionally minimal: energy accounting, quantization handling,
  and advanced model lifecycle management should be added in follow-up work.
- The test provided in reference-tests/test_llama_runtime.py uses a monkeypatched
  dummy llama_cpp module and runs quickly in CI without native deps.
