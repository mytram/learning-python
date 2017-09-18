# coding: utf-8

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from common import calculate_prime_factors

def perm_divisors(prime_counts):
    divisors = [1]
    for prime, times in prime_counts.items():
        sub_prime_counts = dict(prime_counts)
        del sub_prime_counts[prime]
        sub_divisors = perm_divisors(sub_prime_counts)
        for sub_divisor in sub_divisors:
            for i in range(0, times + 1):
                divisors.append(prime ** i * sub_divisor)

    return divisors

def calculate_proper_divisors(n):
    prime_factors = calculate_prime_factors(n)
    prime_counts = {}
    for p in prime_factors:
        prime_counts[p] = prime_counts.get(p, 0) + 1

    return set(perm_divisors(prime_counts)) - {n,}

def solve(problem=10_000):
    amicable_numbers = {0: 0, 1: 1}
    for n in range(2, problem):
        divisors = calculate_proper_divisors(n)
        amicable_numbers[n] = sum(divisors)

    return sum(number for number, dn in amicable_numbers.items() if amicable_numbers.get(dn, 0) == number and number != dn)

if __name__ == '__main__':
    print(__file__ + ": %d" % solve(10_000))
