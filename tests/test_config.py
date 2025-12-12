from pathlib import Path

from open_rl_trainer.utils.config import load_config


def test_load_config_default():
    config_path = Path(__file__).resolve().parents[1] / "configs" / "default.yaml"
    config = load_config(config_path)
    assert config["environment"]["game"] == "go"
    assert config["network"]["architecture"] == "resnet"
