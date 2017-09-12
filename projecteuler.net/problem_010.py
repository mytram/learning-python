# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from common import PrimeGenerator

def solve():
    g = PrimeGenerator(2_000_000)
    return sum(g)

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
