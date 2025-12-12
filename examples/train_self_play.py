from pathlib import Path

from open_rl_trainer.training.mcts import MCTS
from open_rl_trainer.training.self_play import SelfPlayTrainer
from open_rl_trainer.utils.config import load_config


def main() -> None:
    config = load_config(Path(__file__).resolve().parents[1] / "configs" / "default.yaml")
    trainer = SelfPlayTrainer(num_games=config["training"]["self_play_games"])
    mcts = MCTS(simulations=16)
    trajectories = list(trainer.generate(mcts))
    print(f"Generated {len(trajectories)} placeholder self-play trajectories")


if __name__ == "__main__":
    main()
