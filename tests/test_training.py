from open_rl_trainer.training.mcts import MCTS
from open_rl_trainer.training.self_play import SelfPlayTrainer
from open_rl_trainer.training.supervised import SupervisedTrainer
from open_rl_trainer.data.dataset import TrajectorySample


def test_supervised_trainer_counts_samples():
    trainer = SupervisedTrainer()
    samples = [TrajectorySample(state={}, action={}, reward=0.0, next_state={}, done=False) for _ in range(3)]
    loss = trainer.train_epoch(samples)
    assert loss == 3.0


def test_self_play_generates():
    trainer = SelfPlayTrainer(num_games=2)
    mcts = MCTS(simulations=4)
    games = list(trainer.generate(mcts))
    assert len(games) == 2
    assert all(g["simulations"] == 4 for g in games)
