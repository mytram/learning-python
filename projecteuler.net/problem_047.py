# coding: utf-8

# Distinct primes factors
# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


from common import calculate_prime_factors

def solve():
    n = 647
    numbers = []
    while True:
        factors = calculate_prime_factors(n)
        if len(set(factors)) == 4:
            numbers.append(n)
        else:
            numbers = []
        if len(numbers) == 4:
            return numbers[0]
        n += 1

if __name__ == '__main__':
    print(__file__ + ": %s" % solve())
