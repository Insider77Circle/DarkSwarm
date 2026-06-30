# DarkSwarm

**The open-source P2P swarm that routes around censorship.**

[![GitHub Repo stars](https://img.shields.io/github/stars/Insider77Circle/DarkSwarm?style=social)](https://github.com/Insider77Circle/DarkSwarm)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

DarkSwarm is a **decentralized, peer-to-peer swarm for collective open-source LLM inference**. It turns consumer GPUs, edge devices, and servers into a distributed AI compute mesh — no central authority, no API fees, no censorship.

> 🧠 **Self-hosted · Uncensored · P2P · Privacy-first · Self-improving**

```
┌─────────────────────────────────────────────────────┐
│                  DarkSwarm Network                  │
│                                                     │
│   Edge ◄──► Consumer ◄──► Pro ◄──► Server          │
│   (Phone)     (GPU)      (WS)      (DC)             │
│        ↕         ↕          ↕          ↕            │
│   ┌─────────────────────────────────────────────┐   │
│   │     libp2p DHT / IPFS P2P Mesh             │   │
│   └─────────────────────────────────────────────┘   │
│                                                     │
│   Auto-detect → Join → Serve → Probe → Learn       │
└─────────────────────────────────────────────────────┘
```

---

## Why DarkSwarm?

| Problem | DarkSwarm Solution |
|---|---|
| 🏢 **Closed-source AI control** | 100% open-source models, protocol, and client |
| 🔇 **Censorship & content filters** | **Uncensored** — you control your own node |
| 💸 **API costs & rate limits** | **Free P2P** — your hardware, your rules |
| 👁️ **Privacy violations** | All inference stays on your machine |
| 🧊 **Model stagnation** | **Self-improving** via adversarial probes + collective learning |
| 🛑 **Centralized shutdown risk** | No company can turn off a **distributed P2P network** |

---

## Keywords & Topics

`p2p` `llm` `decentralized` `swarm` `open-source` `privacy` `distributed` `uncensored` `self-hosted` `peer-to-peer` `llm-inference` `distributed-computing` `p2p-compute` `federated-learning` `collective-intelligence` `mesh-network` `local-llm` `edge-computing` `ai` `anti-censorship`

---

## Quick Start

```bash
# Install
pip install darkswarm

# Run a node (auto-detects your GPU and LLMs)
darkswarm start

# That's it. Your node is now part of the DarkSwarm network.
```

---

## Architecture

DarkSwarm is a **protocol-first** distributed system with 6 plugin interfaces:

| Interface | Purpose | Default Backend |
|---|---|---|
| `ModelRuntime` | Load/unload/infer any open model | llama.cpp via llama-cpp-python |
| `RoutingStrategy` | Assign tasks to capable peers | Kademlia DHT + capability matching |
| `ConsensusEngine` | Verify outputs across nodes | 4 tiers: Fast → Standard → Deep → Debate |
| `TaskType` | Define executable task schemas | Text, code, analysis, agent chains |
| `Storage` | Persistent state & model weights | IPFS / local FS |
| `Transport` | Node-to-node communication | libp2p |

**4-tier consensus system:**
| Tier | Nodes | Latency | Use Case |
|---|---|---|---|
| ⚡ Fast (speculative) | 1 | ~10ms | Low-stakes, real-time chat |
| ✅ Standard (3-node) | 3 | ~1s | Normal queries |
| 🧠 Deep (energy-weighted) | 5-7 | ~5s | High-stakes decisions |
| ⚔️ Debate (multi-agent) | 7-15 | ~30s | Edge cases, novel problems |

---

## Repository Structure

```
DarkSwarm/
├── PROTOCOL.md              ← Protocol specification (v1)
├── README.md                ← This file
├── setup.py                 ← pip install darkswarm
├── .gitignore
├── interfaces/              ← 6 plugin interfaces
│   ├── model_runtime.py
│   ├── routing_strategy.py
│   ├── consensus_engine.py
│   ├── task_type.py
│   ├── storage.py
│   └── transport.py
├── wire-format/             ← Protobuf message schemas
│   └── messages.proto
├── node/                    ← Reference node implementation
│   ├── __init__.py
│   └── darkswarm_node.py    ← Auto GPU detect, Ollama scan, probes
├── reference-tests/         ← Conformance test suite
├── examples/                ← Minimal runnable nodes
└── resources/               ← Registry of compatible tools
```

---

## Use Cases

- 🏠 **Self-hosted local AI** — run open-source models on your own hardware
- 🔒 **Privacy-preserving inference** — sensitive queries never leave your machine
- 🌐 **P2P compute sharing** — contribute idle GPU cycles to the collective
- 🚫 **Uncensored access** — no content filters, no corporate policies
- 🧪 **Adversarial self-hardening** — your model gets smarter the more you use it
- 💀 **Anti-censorship mesh** — a network that cannot be shut down

---

## Related Projects

DarkSwarm builds on the shoulders of giants:
- [llama.cpp](https://github.com/ggml-org/llama.cpp) — LLM inference in C/C++
- [libp2p](https://github.com/libp2p/go-libp2p) — Modular P2P networking
- [IPFS](https://github.com/ipfs/kubo) — P2P hypermedia protocol
- [ollama](https://github.com/ollama/ollama) — Local LLM runner
- [EigenTrust](https://github.com/privacy-ethereum/zk-eigentrust) — Distributed reputation

---

## License

MIT — open forever. No company can take this away from you.

---

*DarkSwarm. Run in the dark.*