from dataclasses import dataclass
from typing import Iterable

from open_rl_trainer.training.mcts import MCTS


@dataclass
class SelfPlayTrainer:
    """Self-play loop coordinating rollouts with MCTS."""

    num_games: int = 1

    def generate(self, mcts: MCTS) -> Iterable[dict]:
        for _ in range(self.num_games):
            yield mcts.run()
