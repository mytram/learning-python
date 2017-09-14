# coding: utf-8

# Factorial digit sum
# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import functools
import operator

def factorial(n):
    return sum(
        int(x) for x in str(functools.reduce(operator.mul, range(1, n+1)))
    )

def solve(n = 100):
    return factorial(n)

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
