from dataclasses import dataclass
from typing import Any


@dataclass
class DiscretePolicyHead:
    action_dim: int

    def __call__(self, logits: Any) -> Any:  # pragma: no cover - placeholder
        return logits


@dataclass
class ContinuousPolicyHead:
    action_dim: int

    def __call__(self, params: Any) -> Any:  # pragma: no cover - placeholder
        return params
