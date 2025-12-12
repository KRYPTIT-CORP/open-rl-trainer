from pathlib import Path


def export_stub(model, path: Path | str) -> None:  # pragma: no cover - placeholder
    """Placeholder export that writes a note to disk."""
    Path(path).write_text("Export not implemented. Provide TorchScript/ONNX export.")
