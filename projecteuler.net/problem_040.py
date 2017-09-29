# coding: utf-8

# Champernowne's constant
# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import functools

def solve():
    constant = ''.join(str(i) for i in range(1, 185186))
    #
    # I discovered 185186 by the following code first:
    # i = 100000
    # while len(constant) < 1000000:
    #     constant += str(i)
    #     i +=1
    #
    # print(i) # 185186

    return functools.reduce(
        lambda prod, x: prod * int(constant[x - 1]),
        (1, 10, 100, 1000, 10000, 100000, 1000000),
        1
    )

if __name__ == '__main__':
    print(__file__ + ': ', solve())
