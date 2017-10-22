# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from common import PrimeGenerator

def solve(problem = 20):
    number = 1
    primes = list(PrimeGenerator(problem + 1))

    for factor in range(2, problem + 1):

        while number % factor != 0:
            for p in primes:
                if factor % p == 0:
                    number *= p
                    break
    return number

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
