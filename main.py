from game import TicTacToe
from mcts import Node, search
from collections import deque

def main():
    print("Hello, World!")
    
    env = TicTacToe()
    root = search(None, env, 10000)


if __name__ == "__main__":
    main()
