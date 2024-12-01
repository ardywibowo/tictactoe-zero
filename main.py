from game import TicTacToe
from mcts import search, play

def main():
    env = TicTacToe()
    root = search(None, env, 1000000)
    while True:
        play(root, env)

if __name__ == "__main__":
    main()
