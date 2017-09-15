# Lexicographic permutations
# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


def lex_perm(digits):
    if len(digits) == 1:
        yield digits
        return

    for head in digits:
        tail = [x for x in digits if x != head]
        for sub_perm in lex_perm(tail):
            yield [head] + sub_perm

def solve(problem):
    for index, result in enumerate(lex_perm(problem)):
        if index == 1_000_000 - 1:
            return ''.join(str(d) for d in result)

if __name__ == '__main__':
    print(__file__ + ": %s" % solve(list(range(0,10))))
