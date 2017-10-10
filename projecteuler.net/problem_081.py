# coding: utf-8

#
# Path sum: two ways
# Problem 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down

# dijkstra's algorithm

import math

def find_shortest_path(matrix):
    unvisited_matrix = {}

    row_count = len(matrix)
    col_count = len(matrix[row_count - 1])

    for row in range(row_count):
        for col in range(len(matrix[row])):
            unvisited_matrix[(row, col)] = [math.inf, matrix[row][col]]

    unvisited_matrix[(0,0)][0] = unvisited_matrix[(0,0)][1]
    start_point = (0, 0)
    finish_point = (row_count - 1, col_count - 1)
    visited = []

    while start_point != finish_point:
        row, column = start_point
        distance, _ = unvisited_matrix.get(start_point)

        right = unvisited_matrix.get((row, column + 1), None)
        down  = unvisited_matrix.get((row + 1, column), None)

        for node in (right, down):
            if node == None: continue
            new_distance = distance + node[1]
            if node[0] > new_distance: node[0] = new_distance

        del unvisited_matrix[start_point]
        visited.append(start_point)

        min_point, min_distance = None, math.inf

        for point, value in unvisited_matrix.items():
            if min_distance > value[0]:
                min_distance = value[0]
                min_point = point

        start_point = min_point

    return unvisited_matrix[finish_point]

def read_matrix():
    matrix = []
    with open('p081_matrix.txt', 'r') as f:
        for line in f:
            matrix.append(list(map(int, line.strip().split(','))))

    return matrix

def test_matrix():
    return [[131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331]]

def solve():
    matrix = read_matrix()
    return find_shortest_path(matrix)

if __name__ == '__main__':
    print(__file__ + ':', solve())
