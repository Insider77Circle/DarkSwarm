# DarkSwarm

**P2P decentralized swarm for local LLM inference — self-hosted llama.cpp mesh (no API fees).**

[![GitHub stars](https://img.shields.io/github/stars/Insider77Circle/DarkSwarm?style=social)](https://github.com/Insider77Circle/DarkSwarm/stargazers) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) [![Issues](https://img.shields.io/github/issues/Insider77Circle/DarkSwarm)](https://github.com/Insider77Circle/DarkSwarm/issues)


Table of contents

- [Quickstart](#quickstart-example)
- [Features](#features)
- [Getting started](#getting-started)
- [Contributing & Code of Conduct](#contributing--code-of-conduct)
- [Topics & SEO keywords](#topics--seo-keywords)
- [Contact & Community](#contact--community)
- [Docs](#docs)


DarkSwarm is an open-source, peer-to-peer compute mesh that enables local LLM inference across self-hosted nodes using llama.cpp. It is privacy-focused, censorship-resistant, and designed to avoid central API fees by running inference on participant machines.

Why DarkSwarm?

- Self-hosted LLM inference: run models locally across a P2P mesh.
- llama.cpp integration: compatible with local LLM runtimes (llama.cpp-style backends).
- Privacy-first and decentralized: no central authority, control stays with node operators.
- Designed for edge and distributed deployments (low-latency local compute pooling).

Quickstart (example)

Copy-paste this 1-line quickstart to get a node running (adjust MODEL_PATH and NODE_NAME):

```bash
python3 -m pip install -r requirements.txt && python3 run_node.py --model /path/to/model --name my-node-01
```

For a fuller example and Docker instructions see docs/QUICKSTART.md.

Features

- Peer-to-peer node discovery and routing
- Distributed inference pipelines and batching
- Load balancing and latency-aware scheduling
- Simple web UI (HTML frontend) for monitoring and demoing nodes

Getting started

1. Read docs/QUICKSTART.md for a one-command example to get a node running.
2. See docs/ARCHITECTURE.md for an overview of the mesh, protocol, and security model.
3. Check CONTRIBUTING.md to learn how to run tests and submit PRs.

Contributing & Code of Conduct

We welcome contributions. LICENSE (MIT) is included — see LICENSE for details. CONTRIBUTING.md and CODE_OF_CONDUCT.md are present with contributor guidelines and behavior expectations.

Topics & SEO keywords (use as GitHub Topics / headings in the README):

- p2p
- peer-to-peer
- decentralized-ai
- distributed-ai
- local-llm
- self-hosted
- llama.cpp
- llama-cpp
- open-source
- inference
- privacy
- mesh-network
- federated-learning
- edge-computing
- distributed-computing
- python
- html
- privacy-preserving
- no-api-fees
- swarm

Note: These topics should be applied in Settings → Topics (or via the Topics API) so they appear on the repository page.

Contact & Community

Open an issue or discussion for questions, feature requests, and community coordination.

---

<!-- Historical content removed from the top-level README and can be found in docs/OLD_README.md if needed. -->
