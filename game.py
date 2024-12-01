import random

class TicTacToe:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.valid_moves = set([(i, j) for i in range(3) for j in range(3)])
        
        self.player = 1
    
    def print_board(self):
        for i, row in enumerate(self.board):
            row = ['O' if cell == 1 else 'X' if cell == -1 else ' ' for cell in row]
            print('|'.join(row))
            
            if i != len(self.board) - 1:
                print('-' * 5)
        
        print(' ')
    
    def random_move(self):
        return random.choice(list(self.valid_moves))
    
    def step(self, action):
        x, y = action
        
        observation = self.board.copy()
        if self.board[x][y] != 0:
            reward = -1
            terminated = True
            truncated = True
            return observation, -10, terminated, truncated
        
        self.board[x][y] = self.player
        self.valid_moves.remove((x, y))
        self.player *= -1
        
        reward = self.check_winner()
        terminated = reward != 0 or len(self.valid_moves) == 0
        truncated = False
        return observation, reward, terminated, truncated
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return self.board[0][i]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        
        return 0


if __name__ == "__main__":
    game = TicTacToe()
    game.print_board()
    winner = game.check_winner()
    print('Winner:', 'O' if winner == 1 else 'X' if winner == -1 else 'None')
    
    print(game.step((0, 0)))
    game.print_board()
    print(game.step((0, 1)))
    game.print_board()
    print(game.step((1, 1)))
    game.print_board()
    print(game.step((0, 2)))
    game.print_board()
    winner = game.check_winner()
    print('Winner:', 'O' if winner == 1 else 'X' if winner == -1 else 'None')
    
    print(game.step((2, 2)))
    game.print_board()
    
    winner = game.check_winner()
    print('Winner:', 'O' if winner == 1 else 'X' if winner == -1 else 'None')
