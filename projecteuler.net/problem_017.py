# Number letter counts
# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
# total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342
# (three hundred and forty-two) contains 23 letters and 115 (one hundred and
# fifteen) contains 20 letters. The use of "and" when writing out
# numbers is in compliance with British usage.
#
dictionary = {
    1: len('one'),
    2: len('two'),
    3: len('three'),
    4: len('four'),
    5: len('five'),
    6: len('six'),
    7: len('seven'),
    8: len('eight'),
    9: len('nine'),
    10: len('ten'),
    11: len('eleven'),
    12: len('twelve'),
    13: len('thirteen'),
    14: len('fourteen'),
    15: len('fifteen'),
    16: len('sixteen'),
    17: len('seventeen'),
    18: len('eighteen'),
    19: len('nineteen'),
    20: len('twenty'),
    30: len('thirty'),
    40: len('forty'),
    50: len('fifty'),
    60: len('sixty'),
    70: len('seventy'),
    80: len('eighty'),
    90: len('ninety'),
    100: len('hundred'),
    1000: len('thousand')
}

def count_number_letters_0_99():
    count_0_9 = sum(dictionary.get(n) for n in range(1, 10))
    count = sum(dictionary.get(n) for n in range(1, 20)) # 1 - 19
    count += sum(dictionary.get(tens * 10) * 10 for tens in range(2, 10)) # 20, 30, 40, 50, 60, 70, 80, 90
    return count + count_0_9 * 8

# @WARNING: UNREADABLE
def solve():
    count_0_99 = count_number_letters_0_99()
    count_hundreds = len('and') * 99 + dictionary.get(100) * 100 + count_0_99
    total = sum(dictionary.get(h) for h in range(1, 10)) * 100 + count_hundreds * 9
    return dictionary.get(1) + dictionary.get(1000) + count_0_99 + total

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
