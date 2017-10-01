# coding: utf-8

# Coded triangle numbers
# Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word
# value. For example, the word value for SKY is 19 + 11 + 25 = 55 =
# t10. If the word value is a triangle number then we shall call the
# word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K
# text file containing nearly two-thousand common English words, how
# many are triangle words?

import re

class TriangleNumbers:
    triangle_number_dict = {1:1}
    reverse_triangle_number_dict = {1:1}

    def __init__(self):
        self.generate_upto(1_000)

    @classmethod
    def is_triangle_number(klass, number):
        klass.generate_upto(number + 1)
        return number in klass.reverse_triangle_number_dict

    @classmethod
    def generate_upto(klass, x):
        if len(klass.triangle_number_dict) == 0:
            klass.triangle_number_dict = {1: 1}
            klass.reverse_triangle_number_dict = {1: 1}

        max_n = max(klass.triangle_number_dict.keys())
        max_number = klass.triangle_number_dict[max_n]

        while max_number < x:
            max_n += 1
            max_number += max_n
            klass.triangle_number_dict[max_n] = max_number
            klass.reverse_triangle_number_dict[max_number] = max_n

def find_triangle_number():
    la = ord('A')
    a_to_i_dict = dict((chr(n + la - 1), n) for n in range(1, 27))

    tri = TriangleNumbers
    with open('p042_words.txt', 'r') as f:
        lines = f.readlines()
        words = re.sub(r'[\s"]', '', ''.join(lines).upper()).split(',')

    for word in words:
        word_value = sum(a_to_i_dict[a] for a in word)
        if tri.is_triangle_number(word_value):
            yield (word_value, word)

def solve():
    return len(tuple(find_triangle_number()))

if __name__ == '__main__':
    print(__file__ + ':', solve())
