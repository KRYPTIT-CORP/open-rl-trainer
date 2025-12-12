def elo_delta(win_rate: float, k: int = 32) -> float:
    """Compute a simple Elo delta from win rate."""
    return k * (win_rate - 0.5)
