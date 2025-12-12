from open_rl_trainer.evaluation.arena import Arena


def main() -> None:
    arena = Arena(episodes=3)
    result = arena.evaluate(lambda _: 1, lambda _: 0)
    print(f"Placeholder evaluation win rate: {result}")


if __name__ == "__main__":
    main()
