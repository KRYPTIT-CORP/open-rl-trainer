from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Mapping, Sequence
import json


@dataclass
class TrajectorySample:
    state: Mapping
    action: Mapping
    reward: float
    next_state: Mapping
    done: bool


class TrajectoryDataset(Sequence[TrajectorySample]):
    """
    Minimal trajectory dataset backed by JSON lines.
    Intended as a placeholder until game-specific adapters are added.
    """

    def __init__(self, path: Path | str):
        self.path = Path(path)
        self._data: List[TrajectorySample] = []
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            raise FileNotFoundError(f"Trajectory file not found: {self.path}")
        with self.path.open() as f:
            for line in f:
                payload = json.loads(line)
                self._data.append(TrajectorySample(**payload))

    def __len__(self) -> int:  # pragma: no cover - trivial
        return len(self._data)

    def __getitem__(self, idx: int) -> TrajectorySample:
        return self._data[idx]

    def __iter__(self) -> Iterator[TrajectorySample]:  # pragma: no cover - trivial
        return iter(self._data)

    @classmethod
    def from_iterable(cls, samples: Iterable[TrajectorySample], path: Path | str) -> "TrajectoryDataset":
        path = Path(path)
        with path.open("w") as f:
            for sample in samples:
                f.write(json.dumps(sample.__dict__) + "\n")
        return cls(path)
