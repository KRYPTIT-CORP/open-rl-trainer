from typing import Iterable

from .dataset import TrajectorySample


def validate_trajectory(samples: Iterable[TrajectorySample]) -> bool:
    """
    Simple validation to ensure each sample has required fields.
    Returns True if all samples contain non-null states and actions.
    """
    for sample in samples:
        if sample.state is None or sample.action is None:
            return False
    return True
