"""Training loops for supervised learning and self-play."""

from .supervised import SupervisedTrainer
from .self_play import SelfPlayTrainer

__all__ = ["SupervisedTrainer", "SelfPlayTrainer"]
