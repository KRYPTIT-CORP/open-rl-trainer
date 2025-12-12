from __future__ import annotations

from typing import Protocol, Tuple


class PolicyValueNetwork(Protocol):
    """
    Protocol for combined policy/value networks.
    Concrete implementations may use PyTorch, JAX, or another backend.
    """

    def forward(self, observation) -> Tuple[object, float]:
        ...
