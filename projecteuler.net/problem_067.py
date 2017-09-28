# Maximum path sum II
# Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

def solve(problem):
    problem = problem
    traversal = []
    for row in problem:
        traversal.append(tuple([int(node), int(node)] for node in row))

    size = len(traversal)
    for row, nodes in enumerate(traversal):
        row_size = len(nodes)
        # update connected nodes
        next_row = row + 1
        if next_row == size:
            break

        for col, node in enumerate(nodes):
            for c in (col, col +1):
                connected_node = traversal[next_row][c]
                distance = node[1] + connected_node[0]
                if  distance > connected_node[1]:
                    connected_node[1] = distance

    return max(node[1] for node in traversal[-1])

def get_triangle():
    with open('triangle.txt', 'r') as f:
        triangle = tuple(tuple(line.split()) for line in f)
    return triangle

if __name__ == '__main__':
    print(__file__, ': ', solve(get_triangle()))
