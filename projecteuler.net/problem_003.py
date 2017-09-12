# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
#

from common import PrimeGenerator

def solve(problem = 600_851_475_143):
    series = PrimeGenerator()
    prime = next(series)

    while prime < problem:
        if problem % prime == 0:
            return solve(problem / prime)
        prime = next(series)

    return problem

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
