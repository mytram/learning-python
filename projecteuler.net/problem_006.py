# coding: utf-8
#
# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

def solve(problem = 100):
    numbers = range(1, problem+1)
    total = sum(numbers)
    return total * total - sum(x * x for x in numbers)

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
