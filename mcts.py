from typing import Optional
import math

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.children = {}
        self.visits = 0
        self.value = 0
    
    def select_child(self):
        if not self.children:
            return None
        
        return max(
            self.children.items(), 
            key=lambda x: (x[1].value / x[1].visits + math.sqrt(2 * math.log(self.visits) / x[1].visits) if x[1].visits > 0 else float('inf'))
        )
    
    def expand(self, env):
        for move in env.valid_moves:
            self.children[move] = Node(self)
    
    def update(self, value):
        node = self
        while node:
            node.visits += 1
            node.value += value
            node = node.parent

def search(root: Optional[Node], env, num_simulations):
    if not root:
        root = Node(None)
    
    for i in range(num_simulations):
        node = root
        env.reset()
        terminated, truncated = False, False
        while not terminated and not truncated:
            if not node.children:
                node.expand(env)
                move, node = node.select_child()
                observation, reward, terminated, truncated = env.step(move)
                break
            else:
                move, node = node.select_child()
                observation, reward, terminated, truncated = env.step(move)
        
        # Rollout
        while not terminated and not truncated:
            move = env.random_move()
            observation, reward, terminated, truncated = env.step(move)
        
        node.update(reward)
    
    return root
