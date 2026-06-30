# DarkSwarm

**The open-source P2P swarm that routes around censorship.**

DarkSwarm is a decentralized protocol and reference node implementation for collective open-source LLM inference. It enables a global P2P network of consumer devices to share compute, models, and intelligence — with no central authority, no API fees, and no censorship.

```
┌─────────────────────────────────────────────────────┐
│                  DarkSwarm Network                  │
│                                                     │
│   Edge ◄──► Consumer ◄──► Pro ◄──► Server          │
│   (Phone)     (GPU)      (WS)      (DC)             │
│        ↕         ↕          ↕          ↕            │
│   ┌─────────────────────────────────────────────┐   │
│   │           libp2p DHT / IPFS Mesh            │   │
│   └─────────────────────────────────────────────┘   │
│                                                     │
│   Auto-detect → Join → Serve → Probe → Learn       │
└─────────────────────────────────────────────────────┘
```

## Why DarkSwarm?

| Problem | DarkSwarm Solution |
|---|---|
| Closed-source AI control | 100% open-source models, protocol, and client |
| Censorship & content filters | Uncensored — you control your own node |
| API costs & rate limits | Free P2P — your hardware, your rules |
| Privacy | All inference stays on your machine by default |
| Model stagnation | Self-improving via adversarial probes + collective learning |
| Centralized shutdown risk | No company can turn off a P2P network |

## Quick Start

```bash
# Install
pip install darkswarm

# Run a node (auto-detects your GPU and LLMs)
darkswarm start

# That's it. Your node is now part of DarkSwarm.
```

## Architecture

DarkSwarm is designed as a **protocol-first** system with 6 plugin interfaces:

| Interface | Purpose | Default Backend |
|---|---|---|
| `ModelRuntime` | Load/unload/infer any open model | llama.cpp via llama-cpp-python |
| `RoutingStrategy` | Assign tasks to capable peers | Kademlia DHT + capability matching |
| `ConsensusEngine` | Verify outputs across nodes | 4 tiers: Fast → Standard → Deep → Debate |
| `TaskType` | Define executable task schemas | Text, code, analysis, agent chains |
| `Storage` | Persistent state & model weights | IPFS / local FS |
| `Transport` | Node-to-node communication | libp2p |

## Repository Structure

```
DarkSwarm/
├── PROTOCOL.md              ← The spec. Everything depends on this.
├── interfaces/              ← 6 plugin interfaces
├── wire-format/             ← Protobuf message schemas
├── node/                    ← Reference node implementation
├── reference-tests/         ← Conformance test suite
├── examples/                ← Minimal nodes
└── resources/              ← Registry of compatible open-source tools
```

## License

MIT — open forever.

---

*DarkSwarm. Run in the dark.*