import numpy as np
import os

#Initialize 8*8 grid
def initialize_grid(size, randomize=False):
    if randomize:
        return np.random.randint(2, size=(8, 8))
    else:
        return np.zeros((8, 8), dtype=int)

# Print 8*8 grid
def print_grid(grid):
    # os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in grid:
        print(' '.join(['█' if cell else ' ' for cell in row]))

#Update the grid with l_cell(live_cell) and d_cell(dead cell)
def grid_update(grid):
        gridcopy = grid.copy()

        for i in range(grid[0]):
            for j in range(grid[1]):
                
                l_cell = sum(
                    [grid[[i], (j-1)], 
                     ]
                )





                # Conway's rule
                if grid[i,j]==1:
                    if l_cell < 2 or l_cell>3:
                        gridcopy[i,j]==0
                else:
                    if l_cell==3:
                        gridcopy[i,j] ==1
                
        return gridcopy






















if __name__ == "__main__":
    run(size=20, randomize=True, iterations=100, delay=0.1)