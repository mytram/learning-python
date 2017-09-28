# Circular primes
# Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

from common import PrimeGenerator, l_to_i, is_prime

def rotate(lst):
    for _ in range(len(lst)):
        head, *tail = lst
        lst = tail + [head]
        yield ''.join(lst)

def is_circular_prime(prime, prime_dict):
    digits = str(prime)
    rs = rotate(digits)
    return all(prime_dict.get(n, False) for n in rs)

def solve():
    primes = list(PrimeGenerator(lt = 1_000_000))
    prime_dict = dict((str(prime), True) for prime in primes)

    return tuple(prime for prime in primes if is_circular_prime(prime, prime_dict))

if __name__ == '__main__':
    print(__file__ + ':', len(solve()))
