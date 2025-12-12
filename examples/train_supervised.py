from pathlib import Path

from open_rl_trainer.data.dataset import TrajectoryDataset
from open_rl_trainer.training.supervised import SupervisedTrainer
from open_rl_trainer.utils.config import load_config


def main() -> None:
    config = load_config(Path(__file__).resolve().parents[1] / "configs" / "default.yaml")
    trainer = SupervisedTrainer(learning_rate=config["training"]["learning_rate"])
    dataset_path = Path(config["data"]["path"])
    if dataset_path.exists():
        dataset = TrajectoryDataset(dataset_path)
        loss = trainer.train_epoch(dataset)
        print(f"Supervised training placeholder finished, loss={loss}")
    else:
        print(f"Dataset not found at {dataset_path}, skipping.")


if __name__ == "__main__":
    main()
