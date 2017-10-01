# Digit cancelling fractions
# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced
# mathematician in attempting to simplify it may incorrectly believe
# that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of
# fraction, less than one in value, and containing two digits in the
# numerator and denominator.
#
# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.

import math

def is_digit_cancelling(numerator, denominator):
    numerator_digits = list(str(numerator))
    denominator_digits = list(str(denominator))

    common_digits = set(numerator_digits) & set(denominator_digits)
    if len(common_digits) == 0: return False

    cancelling_digit = common_digits.pop()
    numerator_digits.remove(cancelling_digit)
    denominator_digits.remove(cancelling_digit)
    reduced_numerator = int(''.join(numerator_digits))
    reduced_denominator = int(''.join(denominator_digits))

    if reduced_denominator == 0 or reduced_numerator == 0:
        return False

    gcd = math.gcd(numerator, denominator)
    gcd2 = math.gcd(reduced_numerator, reduced_denominator)

    return (numerator // gcd, denominator //gcd) == (reduced_numerator // gcd2, reduced_denominator // gcd2)

def find_4_special_fractions():
    for numerator in range(10, 100):
        for denominator in range(10, 100):
            if numerator % 10 == 0 and denominator % 10 == 0:
                continue
            elif numerator >= denominator:
                continue
            else:
                if is_digit_cancelling(numerator, denominator):
                    yield (numerator, denominator)

# Multiple attempts due to not reading the question carefully:
#
# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.
#
# So the product is given in its lowest common terms!, and what's the
# denominator

def solve():
    fractions = tuple(find_4_special_fractions())

    if len(fractions) != 4:
        raise RuntimeError('wrong fractions', fractions)

    numerator = 1
    denominator = 1
    for f in fractions:
        numerator *= f[0]
        denominator *= f[1]

    print(fractions)
    gcd = math.gcd(numerator, denominator)
    return denominator // gcd

if __name__ == '__main__':
    print(__file__ + ':', solve())
