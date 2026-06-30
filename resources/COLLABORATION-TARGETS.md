# DarkSwarm — Collaboration Targets

Projects building similar decentralized/P2P AI infrastructure. These are potential collaborators, protocol adopters, or cross-promotion partners.

## Tier 1: High Alignment (P2P + LLM Inference)

| Project | Stars | Description | Why Collaborate |
|---|---|---|---|
| [hyperspace-node](https://github.com/hyperspaceai/hyperspace-node) | 323 | World's largest decentralized P2P AI inference network — 2M+ nodes, 3.6M+ downloads | Massive existing userbase. DarkSwarm protocol could complement their network layer. |
| [aios-cli](https://github.com/hyperspaceai/aios-cli) | 180 | Hyperspace CLI client — 2.7M+ downloads | CLI integration potential. |
| [gaianet-node](https://github.com/GaiaNet-AI/gaianet-node) | 5,025 | Install, run and deploy your own decentralized AI agent service | Strong overlap — decentralized AI nodes. Different approach (agent-focused vs swarm-focused). |
| [wavefy](https://github.com/wavefy/decentralized-llm-inference) | 41 | Decentralized LLM inference organization | Multiple repos around the same concept. |
| [cdi-network](https://github.com/cdi-network/cdi-network) | 0 | Decentralized P2P AI Inference Swarm — browser-native, WebGPU + libp2p + OrbitDB | Almost identical stack choices. Browser node compat. |
| [synapse](https://github.com/rickyparmar-raw/synapse) | 0 | P2P AI inference — split models across machines over libp2p | Same transport layer. Model splitting overlap. |

## Tier 2: Adjacent (P2P Compute / GPU Sharing)

| Project | Stars | Description | Why Collaborate |
|---|---|---|---|
| [agentfm-core](https://github.com/agentnetwork/agentfm-core) | 125 | P2P network turning everyday computers into a decentralized AI supercomputer | Near-identical mission. Protocol interop possible. |
| [cuckoo](https://github.com/cuckoo-network/cuckoo) | 408 | Decentralized AI Model-Serving Platform — GPU-sharing for text-to-image + LLM | GPU sharing economy overlap. |
| [hivecomp](https://github.com/xkazm04/hivecomp) | 0 | P2P GPU compute marketplace | Compute marketplace model. |

## Tier 3: Foundational (Shared Dependencies)

| Project | Stars | Description | Why Collaborate |
|---|---|---|---|
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | 118,769 | LLM inference in C/C++ | Primary ModelRuntime backend. Feature requests benefit us. |
| [ollama](https://github.com/ollama/ollama) | 147,000+ | Local LLM runner | Auto-detected by DarkSwarm. Integration deepens. |
| [libp2p](https://github.com/libp2p/go-libp2p) | 6,000+ | Modular P2P networking | Core transport layer. Protocol compat. |
| [IPFS](https://github.com/ipfs/kubo) | 17,064 | P2P hypermedia protocol | Storage + model distribution layer. |
| [Bittensor](https://github.com/opentensor/bittensor) | 1,500+ | Decentralized AI network protocol | Different architecture but same goal. Cross-pollination. |

## How to Reach Out

**Approach strategy:**
1. Open an **issue** on their repo with a genuine compliment + a specific technical question about integration
2. Mention DarkSwarm's protocol-first design — offer to write a bridge or adapter
3. Cross-link: ask them to open an issue on DarkSwarm repo to continue the discussion

**Suggested opening line template:**
> "I'm building [DarkSwarm](https://github.com/Insider77Circle/DarkSwarm) — an open P2P protocol for collective LLM inference. Our stack uses [libp2p/IPFS/llama.cpp] same as yours. Would you be interested in exploring protocol interop between our projects?"