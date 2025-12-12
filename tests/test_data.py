from pathlib import Path

from open_rl_trainer.data.dataset import TrajectoryDataset, TrajectorySample
from open_rl_trainer.data.preprocessing import validate_trajectory


def test_trajectory_dataset_roundtrip(tmp_path: Path):
    samples = [
        TrajectorySample(state={"s": 1}, action={"a": 1}, reward=1.0, next_state={"s": 2}, done=False),
        TrajectorySample(state={"s": 2}, action={"a": 0}, reward=0.0, next_state={"s": 3}, done=True),
    ]
    path = tmp_path / "traj.jsonl"
    dataset = TrajectoryDataset.from_iterable(samples, path)
    assert len(dataset) == 2
    assert dataset[0].reward == 1.0
    assert validate_trajectory(dataset)
