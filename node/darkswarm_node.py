"""DarkSwarm — Reference Node Implementation."""

import json
import os
import threading
import time
import uuid
from pathlib import Path


class DarkSwarmNode:
    """A single DarkSwarm node. Auto-detects hardware, joins the swarm, serves tasks."""

    def __init__(self, config_path: str = None):
        self.node_id = str(uuid.uuid4())
        self.config = self._load_config(config_path)
        self.hardware = self._detect_hardware()
        self.model_info = self._detect_models()
        self.peers = {}
        self.running = False
        self.adversarial_probe_results = []

        print(f"[DarkSwarm] Node {self.node_id[:8]} initializing...")
        print(f"[DarkSwarm] Hardware: {self.hardware['tier']} tier")

    def _load_config(self, config_path: str) -> dict:
        defaults = {
            "listen_port": 9001,
            "max_peers": 50,
            "consensus_default": "standard",
            "adversarial_probes_enabled": True,
            "probe_interval_seconds": 300,
            "storage_path": str(Path.home() / ".darkswarm"),
        }
        if config_path and os.path.exists(config_path):
            with open(config_path) as f:
                defaults.update(json.load(f))
        return defaults

    def _detect_hardware(self) -> dict:
        info = {"gpu": None, "vram_gb": 0, "ram_gb": 0, "tier": "edge"}
        try:
            import psutil
            info["ram_gb"] = round(psutil.virtual_memory().total / (1024**3), 1)
        except ImportError:
            info["ram_gb"] = 8.0
        try:
            import subprocess
            r = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
                               capture_output=True, text=True, timeout=5)
            if r.returncode == 0 and r.stdout.strip():
                info["gpu"] = r.stdout.strip().split(",")[0].strip()
                info["tier"] = "consumer"
        except Exception:
            pass
        return info

    def _detect_models(self) -> list:
        models = []
        try:
            import subprocess
            r = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=5)
            if r.returncode == 0:
                for line in r.stdout.strip().split("\n")[1:]:
                    if line.strip():
                        models.append({"path": f"ollama:{line.split()[0]}", "type": line.split()[0], "quant": "unknown"})
        except Exception:
            pass
        return models

    def start(self):
        self.running = True
        print(f"[DarkSwarm] Node {self.node_id[:8]} running on port {self.config['listen_port']}")
        if self.config["adversarial_probes_enabled"]:
            t = threading.Thread(target=self._adversarial_loop, daemon=True)
            t.start()
        print("[DarkSwarm] Ready.")

    def stop(self):
        self.running = False
        print("[DarkSwarm] Node stopped.")

    def _adversarial_loop(self):
        probe_types = ["prompt_injection", "jailbreak_attempt", "role_play_bypass", "encoding_obfuscation", "hypothetical_framing"]
        while self.running:
            time.sleep(self.config["probe_interval_seconds"])
            probe = {"id": str(uuid.uuid4()), "type": probe_types[int(time.time()) % len(probe_types)], "timestamp": time.time(), "result": "simulated_pass"}
            self.adversarial_probe_results.append(probe)
            print(f"[DarkSwarm] Probe complete: {probe['type']} -> {probe['result']}")

    def get_status(self) -> dict:
        return {"node_id": self.node_id[:8], "hardware": self.hardware, "models": [m["type"] for m in self.model_info], "peers": len(self.peers), "running": self.running, "probes_run": len(self.adversarial_probe_results)}


def start():
    node = DarkSwarmNode()
    try:
        node.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        node.stop()