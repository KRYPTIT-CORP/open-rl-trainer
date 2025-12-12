from dataclasses import dataclass
from typing import Iterable

from open_rl_trainer.data import TrajectorySample


@dataclass
class SupervisedTrainer:
    """Bootstrap a policy/value model from expert trajectories."""

    learning_rate: float = 1e-3

    def train_epoch(self, data: Iterable[TrajectorySample]) -> float:
        # Placeholder loss computation
        count = 0
        for _ in data:
            count += 1
        return float(count)
