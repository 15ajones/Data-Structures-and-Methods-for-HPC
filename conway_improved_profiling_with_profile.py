"""
conway.py 

A simple Python/matplotlib implementation of Conway's Game of Life.

Author: Mahesh Venkitachalam
"""

import numpy as np

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.array(np.pad(np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N), pad_width=1, mode='constant'))

@profile
def update(grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    neighbours = (grid[0:-2, 0:-2] + grid[0:-2, 1:-1] + grid[0:-2, 2:] +
         grid[1:-1, 0:-2]                 + grid[1:-1, 2:] +
         grid[2:  , 0:-2] + grid[2:  , 1:-1] + grid[2:  , 2:])
    birth = (neighbours == 3*ON) & (grid[1:-1, 1:-1] == 0)
    survive = ((neighbours == 2*ON) | (neighbours == 3*ON)) & (grid[1:-1, 1:-1] == ON)
    grid[...] = 0
    grid[1:-1, 1:-1][birth | survive] = ON

# main() function
def main():
    # set grid size
    N = 100
    # declare grid
    grid = np.array([])
    grid = randomGrid(N)
    for iteration in range(100):
        update(grid, N)
    


# call main
if __name__ == "__main__":
    main()