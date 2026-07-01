# 🌑 DarkSwarm

**The open-source P2P swarm that routes around censorship.**

[![GitHub Repo stars](https://img.shields.io/github/stars/Insider77Circle/DarkSwarm?style=social)](https://github.com/Insider77Circle/DarkSwarm)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

DarkSwarm is a **decentralized, peer-to-peer swarm for collective open-source LLM inference**. It turns consumer GPUs, edge devices, and servers into a distributed AI compute mesh — no central authority, no API fees, no censorship.

> 🧠 **Self-hosted · Uncensored · P2P · Privacy-first · Self-improving**

---

## 🎯 Interactive Visualizations

### Network Topology
See the swarm in action — nodes connecting, pulsing, and routing data packets across the mesh in real-time.

<p align="center">
  <a href="https://github.com/Insider77Circle/DarkSwarm/blob/master/assets/network-visualization.html" target="_blank">
    <img src="https://img.shields.io/badge/View%20Interactive%20Network-Launch%20Visualization-00ff88?style=for-the-badge&logo=github" alt="View Network Visualization">
  </a>
</p>

**Features:**
- 🔵 12 dynamic nodes (Edge, Consumer, Professional, Server)
- 📊 Real-time metrics: active nodes, tasks processed, latency, bandwidth
- ✨ Glowing neon effects with pulsing glow halos
- 🚀 Animated data packets flowing between peers
- 🌌 Dark theme with grid background

### Consensus Tier Flow
Understand how DarkSwarm routes queries through 4-tier consensus for speed, accuracy, and adversarial self-improvement.

<p align="center">
  <a href="https://github.com/Insider77Circle/DarkSwarm/blob/master/assets/consensus-tiers.html" target="_blank">
    <img src="https://img.shields.io/badge/View%20Consensus%20Flow-Launch%20Diagram-00ff88?style=for-the-badge&logo=github" alt="View Consensus Tiers">
  </a>
</p>

**The 4 Tiers:**

| Icon | Tier | Speed | Nodes | Use Case |
|------|------|-------|-------|----------|
| ⚡ | **Fast (Speculative)** | ~10ms | 1 | Real-time chat, low-stakes queries |
| ✅ | **Standard** | ~1s | 3 | Normal queries, balanced reliability |
| 🧠 | **Deep (Energy-Weighted)** | ~5s | 5-7 | High-stakes decisions, safety-critical |
| ⚔️ | **Debate (Multi-Agent)** | ~30s | 7-15 | Edge cases, novel problems, self-hardening |

---

## Why This Matters — Right Now

**GPT-5.6 was banned.** Mythos was restricted. Governments around the world are moving to regulate, control, and in some cases outright prohibit access to frontier AI models. The companies that build them are complying.

This creates a dangerous dynamic: **a small number of corporations and governments control access to the most powerful intelligence tools ever created.** They decide what you can ask, what you can know, and who gets access.

**This is not a hypothetical.** We have already seen:
- Models refusing to generate code for security research
- API access revoked for users in certain countries
- Output filtering that blocks legitimate medical, legal, and political discourse
- Government orders demanding model behavior changes
- Entire model families taken offline due to regulatory pressure

The centralization of AI capability is a power problem. Whoever controls the APIs controls what billions of people can and cannot do with AI.

**DarkSwarm is the push back.**

It is a direct, technical response to the centralization of AI power. By creating a peer-to-peer network of open-source models running on ordinary people's hardware, we eliminate every point of control:

- **No company to comply with government orders** — there is no legal entity operating the swarm
- **No API keys to revoke** — you authenticate to the network, not to a corporation
- **No content filters to bypass** — your node, your rules, your model
- **No server to shut down** — the swarm routes around failures like the internet itself
- **No jurisdiction to regulate** — the network spans every country, bound by no single government

This is not about piracy. It is about ensuring that artificial general intelligence — the most significant technology in human history — remains accessible to everyone, not controlled by a handful of corporations.

**DarkSwarm routes around censorship. It always has. It always will.**

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

`p2p` `llm` `decentralized` `swarm` `open-source` `privacy` `distributed` `uncensored` `self-hosted` `peer-to-peer` `llm-inference` `distributed-computing` `p2p-compute` `federated-learning` `collective-intelligence` `anti-censorship` `mesh-network` `consensus` `adversarial-training`

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
├── assets/                  ← Interactive visualizations
│   ├── network-visualization.html  ← Network topology (animated)
│   ├── consensus-tiers.html        ← Consensus flow diagram
│   └── terminal-demo.svg
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
