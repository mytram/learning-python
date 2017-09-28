# Digit fifth powers
# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def find_sum_of_fifth_powers(stop = 9 ** 5 * 7):
    fifth_powers = {}
    for d in range(0, 10):
        fifth_powers[str(d)] = d ** 5

    for n in range(11, stop + 1):
        if sum(fifth_powers[d] for d in str(n)) == n:
            yield n

def solve():
    return sum(find_sum_of_fifth_powers())

if __name__ == '__main__':
    print(__file__ + ':', solve())
