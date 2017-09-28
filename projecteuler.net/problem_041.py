# Pandigital prime
# Problem 41
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

from common import is_prime
import itertools

def pandigitals(size):
    it = itertools.permutations(range(size, 0, -1))

    while True:
        number = list(next(it))
        if number[0] != 0:
            yield number

def list_to_number(ds):
    number = 0
    for d in ds:
        number = number * 10 + d
    return number

def solve():
    # After checking the forum:
    #
    # Start with 7 (I used 9) and going down.  before 9 and 8 digits are
    # divisible by 3 and therefore none of them cannot be prime.
    #
    for size in range(7, 0, -1):
        numbers = pandigitals(size)
        try:
            while True:
                number = list_to_number(next(numbers))
                if is_prime(number):
                    return number
        except StopIteration:
            pass

    return None

if __name__ == '__main__':
    print(__file__ + ': ', solve())
