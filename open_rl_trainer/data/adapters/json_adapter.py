import json
from pathlib import Path
from typing import Iterable, Iterator, Mapping


def load_jsonl(path: Path | str) -> Iterator[Mapping]:
    """Yield dictionaries from a JSONL trajectory file."""
    path = Path(path)
    with path.open() as f:
        for line in f:
            yield json.loads(line)
