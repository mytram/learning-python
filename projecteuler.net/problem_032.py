# coding: utf-8

# Pandigital products
# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from common import l_to_i

import itertools
#
# old slow (6s) solution
#
def _find_pandigital_identities():
    it = itertools.permutations(range(1, 10))
    for digits in it:
        for i in range(1, 5):
            multiplicand = l_to_i(digits[0:i])
            if multiplicand == 1:
                continue
            for j in range(1, 6 - i):
                multiplier = l_to_i(digits[i:i+j])
                product = l_to_i(digits[i+j:])
                if multiplicand * multiplier == product:
                    yield (multiplicand, multiplier, product)

#
# inspired by bitchboy's one line solution in the forum:
#
# print(sum(set(sum([[a*b for b in range(a, 10**((9-len(str(a)))//2))if ''.join(sorted(''.join(map(str,(a,b,a*b)))))=="123456789"]for a in range(1,10**5)],[]))))
def find_pandigital_identities():
    for multiplicand in range(2, 10**5):
        upper = 10**(5 - len(str(multiplicand)))
        #
        # only care multipliers that are greater than multiplicands
        # to avoid duplicates: 39 * 186, and 186 * 39
        #
        for multiplier in range(multiplicand, upper):
            product = multiplicand * multiplier
            as_str = ''.join(sorted(''.join(map(str, (multiplicand, multiplier, product)))))
            if as_str == '123456789':
                yield (multiplicand, multiplier, product)

def solve():
    return sum(set(each[2] for each in find_pandigital_identities()))

if __name__ == '__main__':
    print(__file__ + ':', solve())
