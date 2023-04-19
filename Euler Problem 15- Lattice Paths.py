# Project Euler -- Promblem 15: Lattice Paths
# https://projecteuler.net/problem=15

import time

n = int(input('Size of grid: '))
start_time = time.time()   # to track how long the program takes to run

# Create an initial grid of zeroes and ones. The numbers on the top row
# and leftmost column represent the number of paths from the top-left
# origin to that point on the grid. The rest of the zeroes are place-
# holders.
grid = [[1 for i in range(n+1)] for i in range(n+1)]
for row in grid:
    row[0] = 0
for row in grid[1:len(row)]:
    for element in range(len(row)):
        if row[element] == 0:
            row[element] = 1
        else:
            row[element] = 0

# Un-comment to print the initial grid.
'''
for row in grid:
    print(row)
'''

# Treating the grid like a Pascal's triangle, each of the interior
# zeroes is replaced with the sum of the digit above and the digit
# to the left.
for row in range(1, len(grid)):
    for element in range(len(grid[row])):
        if (row or element) == 0:
            pass
        grid[row][element] = grid[row-1][element] + grid[row][element-1]

# Un-comment to print a grid showing the total number of paths to any
# point from a corner origin.
'''
for row in grid:
    print(row)
'''


print('Number of routes (a.k.a., lattice paths): {output:,}'.format(output=grid[-1][-1]))
print('This program took', time.time() - start_time, 'seconds to run.')
