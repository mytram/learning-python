# coding: utf-8

# Quadratic primes
# Problem 27
# Euler discovered the remarkable quadratic formula:

# n2+n+41n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39. However, when n=40,402+40+41=40(40+1)+41n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41n=41,412+41+41 is clearly divisible by 41.

# The incredible formula n2−79n+1601n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n2+an+bn2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

# where |n||n| is the modulus/absolute value of nn
# e.g. |11|=11|11|=11 and |−4|=4|−4|=4
# Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0n=0.

from common import is_prime, PrimeGenerator

def prime_count(a, b, known_primes, known_non_primes):
    count = 0
    n = 0
    while True:
        number = n * n + a * n + b
        n += 1

        if known_primes.get(number, False):
            count += 1
            continue

        if known_non_primes.get(number, False):
            return count

        if is_prime(number):
            known_primes[number] = True
            count += 1
        else:
            known_non_primes[number] = True
            return count

def solve():
    max_count = 0
    known_primes = {}
    known_non_primes = {}

    for a in range(-999, 1000, 1):
        for b in range(-999, 1000, 1):
            count = prime_count(a, b, known_primes, known_non_primes)
            if count > max_count:
                max_count = count
                ca, cb = a, b
    return ca * cb

if __name__ == '__main__':
    print(__file__ + ':', solve())
