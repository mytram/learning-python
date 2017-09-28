# Sub-string divisibility
# Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools

def gen_pandigital():
    it = itertools.permutations(range(10))
    while True:
        number = list(next(it))
        if number[0] != 0:
            yield number

# this turns out to be faster than functools.reduce
def list_to_number(ds):
    number = 0
    for d in ds:
        number = number * 10 + d
    return number

def sub_string_divisible(digits, primes):
    for i in range(1, 8):
        sub_number = list_to_number(digits[i:i+3])
        if sub_number % primes[i - 1] != 0:
            return False
    return True

def solve():
    primes = [2, 3, 5, 7, 11, 13, 17]

    return sum(list_to_number(pd) for pd in gen_pandigital() if sub_string_divisible(pd, primes))

if __name__ == '__main__':
    print(__file__ + ':', solve())
