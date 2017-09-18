# Digit factorials
# Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from common import FactorialGenerator

def solve():
    diverge = False
    n = 11
    factorial = FactorialGenerator()
    sums = []
    while not diverge:
        digits = tuple(int(d) for d in str(n))
        sum_of_fac_of_digits = sum(factorial.get(d) for d in digits if d != 0)

        if sum_of_fac_of_digits == n:
            sums.append(sum_of_fac_of_digits)
            print("n: ", n, " sum: ", sum_of_fac_of_digits, sums)

        if n > 100_000_000:
            diverge = True
        n += 1
    return 0

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
