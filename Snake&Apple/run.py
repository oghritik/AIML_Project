import argparse

from snake.game import Game, GameConf, GameMode

# it is a main function 
def main():
    dict_solver = {
        "greedy": "GreedySolver",
        "hamilton": "HamiltonSolver",
        "dqn": "DQNSolver",
    }

    dict_mode = {
        "normal": GameMode.NORMAL,
        "bcmk": GameMode.BENCHMARK,
        "train_dqn": GameMode.TRAIN_DQN,
        "train_dqn_gui": GameMode.TRAIN_DQN_GUI,
    }

    parser = argparse.ArgumentParser(description="Run snake game agent.")
    parser.add_argument(
        "-s",
        default="hamilton",
        choices=dict_solver.keys(),
        help="name of the solver to direct the snake (default: hamilton)",
    )
    parser.add_argument(
        "-m",
        default="normal",
        choices=dict_mode.keys(),
        help="game mode (default: normal)",
    )
    args = parser.parse_args()

    conf = GameConf()
    conf.solver_name = dict_solver[args.s]
    conf.mode = dict_mode[args.m]
    print(f"Solver: {conf.solver_name}   Mode: {conf.mode}")

    Game(conf).run()


if __name__ == "__main__":
    main()
