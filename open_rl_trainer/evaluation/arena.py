from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass
class Arena:
    """Pit two policies against each other to estimate win rate."""

    episodes: int = 1

    def evaluate(self, policy_a: Callable, policy_b: Callable) -> float:
        wins = 0
        for i in range(self.episodes):
            if policy_a(i) == policy_b(i):
                continue
            wins += 1
        return wins / max(1, self.episodes)
