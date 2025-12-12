import logging


def configure_logging(level: int = logging.INFO) -> logging.Logger:  # pragma: no cover - thin wrapper
    logging.basicConfig(level=level)
    return logging.getLogger("open_rl_trainer")
