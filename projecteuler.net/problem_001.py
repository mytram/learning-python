# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def solve():
    max_factor_of_3 = int(999 / 3)
    max_factor_of_5 = int(999 / 5)

    result  = sum(i *  3 for i in range(1, 1 + max_factor_of_3))
    result += sum(i *  5 for i in range(1, 1 + max_factor_of_5) if i % 3 != 0)

    return result

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
