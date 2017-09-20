# coding: utf-8
#
# Lattice paths
# Problem 15
#
# Starting in the top left corner of a 2×2 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the
# bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

def travel_grid(grid_size, x, y, known_paths):
    if x > grid_size or y > grid_size:
        return 0

    if known_paths.get((x, y), None):
        return known_paths[(x, y)]

    steps = 0
    steps += travel_grid(grid_size, x + 1, y, known_paths)
    steps += travel_grid(grid_size, x, y + 1, known_paths)

    known_paths[(x, y)] = steps

    return known_paths[(x, y)]

def solve(grid_size = 20):
    return travel_grid(grid_size, 0, 0,
                       {(grid_size, grid_size): 1})

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
