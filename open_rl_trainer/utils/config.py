from pathlib import Path
from typing import Any, Mapping

import yaml


def load_config(path: str | Path) -> Mapping[str, Any]:
    """Load a YAML configuration file."""
    with Path(path).open() as f:
        return yaml.safe_load(f)
