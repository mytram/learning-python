# Consecutive prime sum
# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# from common import *

def find_it(problem):
    primes = PrimeGenerator(problem)
    lookup = {}
    for p in primes:
        lookup[p] = p
    prime_sums = [0]
    for index, prime in enumerate(primes):
        prime_sums.append(prime + prime_sums[index])

    for i, start in enumerate(primes):
        for j, end in enumerate(primes):
            if j == i+1: next
            if end <= start: next
            a_sum = end - start
            if a_sum >= problem: break
            if lookup.get(a_sum, None):
                yield (a_sum, j)

def solve(problem):
    return max(find_it(problem), key=lambda x: x[1])

if __name__ == '__main__':
    print(__file__ + ": %d %s" % solve(1_000))
