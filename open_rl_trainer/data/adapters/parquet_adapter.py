from pathlib import Path
from typing import Iterator, Mapping


def load_parquet(path: Path | str) -> Iterator[Mapping]:
    """
    Placeholder parquet loader. Intentionally avoids a hard dependency on pandas.
    """
    raise NotImplementedError("Parquet loading requires pandas/pyarrow; install and implement as needed.")
