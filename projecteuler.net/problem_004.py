# coding: utf-8
#
# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is 9009 = 91
# × 99.
#
# Find the largest palindrome made from the product of two 3-digit
# numbers.
#
#
#
def solve():
    a = b = tuple(x for x in range(100, 1000) if x % 10 != 0)
    return sorted(filter(lambda r: str(r[0]) == str(r[0])[::-1],
                         ( (x * y, x, y) for x in a for y in b)),
                  reverse = True)[0]

if __name__ == '__main__':
    print(__file__ + ": %d %d %d" % solve())
