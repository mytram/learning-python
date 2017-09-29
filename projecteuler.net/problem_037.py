# Truncatable primes
# Problem 37
# The number 3797 has an interesting property. Being prime itself, it
# is possible to continuously remove digits from left to right, and
# remain prime at each stage: 3797, 797, 97, and 7. Similarly we can
# work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from common import PrimeGenerator

def is_bi_truncatable(prime, prime_dict):
    digits = str(prime)
    if len(digits) == 1:
        return False

    # from left to right
    for i in range(1, len(digits)):
        number = int(''.join(digits[i:]))
        if not prime_dict.get(number, False):
            return False

    # from right to left
    for length in range(len(digits) - 1, 0, -1):
        number = int(''.join(digits[0:length]))
        if not prime_dict.get(number, False):
            return False

    return True

def solve():
    # once I found the greatest prime of the group is 739397, I give
    # it an upper bound to speed it up. cheating :-)
    primes = PrimeGenerator(lt=739398)
    prime_dict = {}
    bi_truncatable_primes = []
    while len(bi_truncatable_primes) < 11:
        prime = next(primes)
        prime_dict[prime] = True
        if is_bi_truncatable(prime, prime_dict):
            bi_truncatable_primes.append(prime)

    print(bi_truncatable_primes)
    return sum(bi_truncatable_primes)

if __name__ == '__main__':
    print(__file__ + ':', solve())
