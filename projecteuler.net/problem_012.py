# Highly divisible triangular number
# Problem 12
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
#  10: 1,2,5,10
#  15: 1,3,5,15
#  21: 1,3,7,21
#  28: 1,2,4,7,14,28
#  We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

from common import PrimeGenerator
import functools
import operator

def calculate_factors(number, prime_generator):
    factors = []
    prime_generator = iter(prime_generator)

    while number != 1:
        prime = next(prime_generator)
        if number % prime == 0:
            number = int(number / prime)
            factors.append(prime)
            prime_generator = iter(prime_generator) # start from 2 again
    return factors

def solve():
    prime_generator = PrimeGenerator()
    triangle_number = 0
    n = 1
    while True:
        triangle_number += n
        n += 1
        factors = calculate_factors(triangle_number, prime_generator)
        if len(factors) == 0: continue
        counts = {}
        for p in factors: counts[p] = counts.get(p, 0) + 1
        divisor_count = functools.reduce(operator.mul, (c+1 for c in counts.values())) + 2 # 1 and triangle_number iteself
        if divisor_count > 500: return triangle_number

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
