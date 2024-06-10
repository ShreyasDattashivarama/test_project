import numpy as np
import os
import time

#Initialize 8*8 grid
def initialize_grid(size, randomize=False):
    if randomize:
        return np.random.randint(2, size=(size, size))
    else:
        return np.zeros((size, size), dtype=int)


# Print 8*8 grid
def print_grid(grid):
    # os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in grid:
        print(' '.join(['*' if cell else ' ' for cell in row]))


#Update the grid with l_cell(live_cell) and d_cell(dead cell)
def grid_update(grid):
        gridcopy = grid.copy()

        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                
                l_cell = sum([
                grid[i, (j-1)%grid.shape[1]],  
                grid[i, (j+1)%grid.shape[1]],  
                grid[(i-1)%grid.shape[0], j],  
                grid[(i+1)%grid.shape[0], j], 
                grid[(i-1)%grid.shape[0], (j-1)%grid.shape[1]], 
                grid[(i-1)%grid.shape[0], (j+1)%grid.shape[1]], 
                grid[(i+1)%grid.shape[0], (j-1)%grid.shape[1]], 
                grid[(i+1)%grid.shape[0], (j+1)%grid.shape[1]]  
            ])
                

            # Conway's rule
            if grid[i,j]==1:
                if l_cell < 2 or l_cell>3:
                    gridcopy[i,j]=0
            else:
                if l_cell==3:
                    gridcopy[i,j]=1
    
        return gridcopy





def run(size=20, randomize=True, iterations=100,delay=0.1):
    grid = initialize_grid(size, randomize)
    for _ in range(iterations):
        print_grid(grid)
        grid = grid_update(grid)
        time.sleep(delay)
        

if __name__ == "__main__":
    run(size=20, randomize=True, iterations=100, delay=10)