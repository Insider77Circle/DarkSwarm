"""DarkSwarm - Open-source P2P LLM swarm."""
from setuptools import setup, find_packages

setup(
    name="darkswarm",
    version="0.1.0",
    description="Open-source P2P swarm for collective LLM inference",
    author="DarkSwarm Contributors",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=["psutil"],
    entry_points={
        "console_scripts": ["darkswarm=node.darkswarm_node:start"],
        "darkswarm.model_runtimes": [
            "mock = node.backends.mock_runtime:MockRuntime",
        ],
    },
)