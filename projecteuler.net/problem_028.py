# Number spiral diagonals
# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def gen_corner_numbers(problem):
    if problem % 2 == 0: return 0

    n = 1
    yield 1
    while n < problem:
        n += 2
        corner = n * n
        yield corner
        for _ in range(3):
            corner -= n - 1
            yield corner

def solve(problem = 1001):
    return sum(gen_corner_numbers(problem))

if __name__ == '__main__':
    print(__file__ + ':', solve())
