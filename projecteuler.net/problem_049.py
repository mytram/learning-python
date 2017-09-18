# coding: utf-8

# Goldberg's other conjecture
# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from common import PrimeGenerator, is_prime
import math

def refute_goldbachs_other_conjecture():
    prime_gen = PrimeGenerator()
    n = 33
    while True:
        n += 2
        if is_prime(n):
            continue
        prime_gen = iter(prime_gen)
        found = False
        for prime in prime_gen:
            if prime >= n: break
            if found: break
            for number in range(1, int(math.sqrt((n - prime)//2)) + 1):
                part = number * number * 2
                conjecture = prime + part
                if conjecture == n:
                    found = True
                    break
        if not found:
            return n

def solve():
    return refute_goldbachs_other_conjecture()

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
