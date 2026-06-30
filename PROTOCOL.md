# DarkSwarm Protocol Specification v1

## 1. Overview

DarkSwarm is a decentralized P2P protocol for collective open-source LLM inference. Nodes coordinate via a DHT mesh to distribute inference tasks, verify outputs through consensus, and improve models through collective learning.

**Key principles:**
- No central authority
- 100% open-source only — no closed-source dependencies
- Self-improving through adversarial probes and collective learning
- Anti-censorship by design

## 2. Node Discovery

Nodes discover each other via a Kademlia DHT (libp2p).

**Node identity:** Each node has a permanent PeerID derived from its public key.

**Capability advertisement:** Each node advertises:
- Model type and size
- Quantization level (2-bit, 4-bit, 8-bit, FP16)
- Available VRAM and RAM
- Tier: Edge (phone), Consumer (GPU), Pro (workstation), Server (datacenter)
- Current load and availability

## 3. Task Routing

Tasks are routed via intent-based capability matching:

1. Client node broadcasts task requirements (model size, latency, trust level)
2. DHT returns nodes matching the capability profile
3. Router selects optimal node(s) based on: capability score, reputation, current load, energy state
4. Task is dispatched

## 4. Consensus — 4 Tiers

| Tier | Mechanism | Nodes | Latency | Use Case |
|---|---|---|---|---|
| Fast | Single local speculative decode | 1 | ~10ms | Low-stakes, real-time |
| Standard | 3-node redundant execution | 3 | ~1s | Normal queries |
| Deep | Energy-weighted consensus | 5-7 | ~5s | High-stakes |
| Debate | Multi-agent adversarial | 7-15 | ~30s | Edge cases |

**Energy-weighted consensus:** A node's vote weight is proportional to its current energy budget (compute availability). High-energy nodes with full models get higher weight.

## 5. Reputation

Based on EigenTrust algorithm:

- Nodes score each other after task completion
- Scores propagate through the DHT
- Low-reputation nodes receive fewer task assignments
- Sybil resistance through computational proof-of-work for new nodes

## 6. Incentives

Nodes that contribute compute earn reputation and priority access. No crypto tokens — pure reciprocity. Contribute more, get faster service when you need help.

## 7. Wire Format

All messages use protobuf serialization (see `wire-format/messages.proto`).

## 8. Versioning

Protocol version `v1`. Backward-compatible extensions via optional fields in protobuf. Breaking changes require a new major version.