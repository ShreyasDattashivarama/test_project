import numpy as np
import os


def initialize_grid(size, randomize=False):
    if randomize:
        return np.random.randint(2, size=(8, 8))
    else:
        return np.zeros((8, 8), dtype=int)
    
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in grid:
        print(' '.join(['█' if cell else ' ' for cell in row]))

