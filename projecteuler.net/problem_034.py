# Digit factorials
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


def solve():
    factorial_dict = {0: 1, 1: 1}
    for n in range(2, 10):
        factorial_dict[n] = n * factorial_dict[n - 1]

    # From the forum:
    # We know that 9! = 362880 has 6 digit
    # and 9! * 7 = 2540160 has 7 digit
    bound = factorial_dict[9] * 7
    number = 3
    total = 0
    while number <= bound:
        fac_sum = sum(factorial_dict[n] for n in map(int, str(number)))
        if number == fac_sum:
            total += number
        number += 1
    return total

if __name__ == '__main__':
    print(__file__ + ':', solve())
