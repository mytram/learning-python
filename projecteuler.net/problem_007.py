# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from common import PrimeGenerator

def solve(problem = 10001):
    g = PrimeGenerator()
    for i in range(0, problem):
        number = next(g)
    return number

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
