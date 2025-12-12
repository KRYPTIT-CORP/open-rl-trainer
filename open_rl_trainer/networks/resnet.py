"""
Placeholder ResNet-style policy/value network.

Implementations should subclass torch.nn.Module and satisfy the PolicyValueNetwork protocol.
"""

from .base import PolicyValueNetwork


class AlphaGoResNet(PolicyValueNetwork):  # pragma: no cover - placeholder
    def __init__(self, observation_shape, action_dim: int, blocks: int = 19):
        self.observation_shape = observation_shape
        self.action_dim = action_dim
        self.blocks = blocks

    def forward(self, observation):
        raise NotImplementedError("Integrate torch and define the dual-head ResNet forward pass.")
