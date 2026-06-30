"""Runtime plugin registry — discover and register ModelRuntime implementations."""

import os
import logging

logger = logging.getLogger(__name__)

_registry = {}


def register_runtime(name, runtime_cls):
    """Register a ModelRuntime implementation class."""
    _registry[name] = runtime_cls
    logger.debug("Registered runtime: %s -> %s", name, runtime_cls.__name__)


def get_runtime(name):
    """Get a registered runtime class by name. Returns None if not found."""
    return _registry.get(name)


def list_runtimes():
    """List all registered runtime names."""
    return list(_registry.keys())


def discover_entry_points():
    """Discover runtimes registered via setuptools entry_points."""
    try:
        from importlib.metadata import entry_points
        eps = entry_points(group="darkswarm.model_runtimes")
        for ep in eps:
            try:
                cls = ep.load()
                register_runtime(ep.name, cls)
                logger.info("Discovered runtime via entry point: %s", ep.name)
            except Exception as e:
                logger.warning("Failed to load entry point %s: %s", ep.name, e)
    except Exception:
        pass


def resolve_runtime(config_runtime=None):
    """Resolve runtime from config, env var, or return None."""
    name = config_runtime or os.environ.get("DARKSWARM_RUNTIME")
    if name:
        cls = get_runtime(name)
        if cls:
            return cls
        logger.warning("Configured runtime '%s' not found in registry", name)
    return None