"""Transformer-based policy/value network placeholder."""

from .base import PolicyValueNetwork


class TransformerBackbone(PolicyValueNetwork):  # pragma: no cover - placeholder
    def __init__(self, observation_shape, action_dim: int, layers: int = 6):
        self.observation_shape = observation_shape
        self.action_dim = action_dim
        self.layers = layers

    def forward(self, observation):
        raise NotImplementedError("Add transformer encoder and heads for policy/value outputs.")
