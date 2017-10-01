# Prime permutations
# Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

from common import PrimeGenerator

def solve():
    primes  = PrimeGenerator(lt = 10 ** 4)

    perms_of_4_digits_primes = {}

    for prime in primes:
        if prime < 1000: continue
        perm_key = ''.join(sorted(str(prime)))

        if perm_key == '1478': continue

        perm_primes = perms_of_4_digits_primes.get(perm_key, [])
        perm_primes.append(prime)
        perms_of_4_digits_primes[perm_key] = perm_primes

    for _, prime_set in perms_of_4_digits_primes.items():
        if len(prime_set) < 3: continue
        for index in range(0, len(prime_set) - 2):
            if prime_set[index + 1] - prime_set[index] == prime_set[index + 2] - prime_set[index + 1]:
                return ''.join(map(str, prime_set[index:index+3]))

if __name__ == '__main__':
    print(__file__ + ':', solve())
