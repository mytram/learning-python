# Non-abundant sums
# Problem 23
# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number. For example, the sum of the
# proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
# that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is
# less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
# smallest number that can be written as the sum of two abundant
# numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two
# abundant numbers. However, this upper limit cannot be reduced any
# further by analysis even though it is known that the greatest number
# that cannot be expressed as the sum of two abundant numbers is less
# than this limit.

# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

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

def find_all_numbers_not_two_abundant_numbers():
    n = 1
    abundant_numbers = {}
    while n <= 28123:
        is_result = True
        for an in abundant_numbers.keys():
            if abundant_numbers.get(n - an, False):
                is_result = False
                break

        if is_result: yield n

        divisors = calculate_proper_divisors(n)

        if sum(divisors) > n:
            abundant_numbers[n] = True

        n += 1

def solve():
    return sum(find_all_numbers_not_two_abundant_numbers())

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
