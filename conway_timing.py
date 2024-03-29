"""
conway.py 

A simple Python/matplotlib implementation of Conway's Game of Life.

Author: Mahesh Venkitachalam
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

ON = 255
OFF = 0
vals = [ON, OFF]


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)


def update(grid, N):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulaton takes place on a toroidal surface.
            total = int(
                (
                    grid[i, (j - 1) % N]
                    + grid[i, (j + 1) % N]
                    + grid[(i - 1) % N, j]
                    + grid[(i + 1) % N, j]
                    + grid[(i - 1) % N, (j - 1) % N]
                    + grid[(i - 1) % N, (j + 1) % N]
                    + grid[(i + 1) % N, (j - 1) % N]
                    + grid[(i + 1) % N, (j + 1) % N]
                )
                / 255
            )
            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    # update data
    grid[:] = newGrid[:]


# main() function
def main(grid_size):
    # set grid size
    N = grid_size




    # declare grid
    grid = np.array([])
    grid = randomGrid(N)
    for iteration in range(100):
        update(grid, N)
    


# call main
if __name__ == "__main__":
    grid_sizes = [10 * i for i in range(1,11)] 
    timings = []
    for grid_size in grid_sizes:
        start_time = time.time()
        main(grid_size)
        end_time = time.time()
        timing = end_time-start_time
        timings.append(timing)
    print(timings)
    plt.plot(grid_sizes, timings)
    plt.xlabel("grid size")
    plt.ylabel("Time taken to execute")
    plt.show()