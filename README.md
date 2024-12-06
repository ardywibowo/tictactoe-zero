# TicTacToe Zero

AlphaZero but for TicTacToe. Actually not even, it's just the MCTS part.

# How to Run

Run the main file. Use `(row) (col)` to index your move:

```
python main.py
```

# Example Game

```
AI move: (1, 2) 0.008218210707507613
 | | 
-----
 | |O
-----
 | | 
 
Enter move: 1 1 
Player move: (1, 1) -0.0009781485309316403
 | | 
-----
 |X|O
-----
 | | 
 
AI move: (2, 0) 0.003857652618381715
 | | 
-----
 |X|O
-----
O| | 
 
Enter move: 0 0
Player move: (0, 0) -0.4430379746835443
X| | 
-----
 |X|O
-----
O| | 
 
AI move: (2, 2) 0.7307692307692307
X| | 
-----
 |X|O
-----
O| |O
 
Enter move: 0 2 
Player move: (0, 2) -0.6923076923076923
X| |X
-----
 |X|O
-----
O| |O
 
AI move: (2, 1) 1.0
X| |X
-----
 |X|O
-----
O|O|O
 
Winner: O
```
