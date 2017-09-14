# coding: utf-8
#
# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at
# 1) contains 10 terms. Although it has not been proved yet (Collatz
# Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#

def collatz_sequence_length(n, known_length):
    problem = n
    sl = known_length.get(n, None)
    if sl != None: return sl

    sl = 0
    if n > 0: sl += 1 # n

    while n > 0:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1

        nl = known_length.get(n, None)
        if nl != None:
            sl += nl
            break

        sl+= 1
        if n <= 1: break

    known_length[problem] = sl
    return sl

def solve(problem = 1_000_000):
    max_len, starting_number  = 0, 0

    known_length = {}
    for p in range(1, problem):
        l = collatz_sequence_length(p, known_length)
        if l > max_len:
            max_len = l
            starting_number = p

    return (starting_number, max_len)

if __name__ == '__main__':
    print(__file__ + ": %s %s" % solve())
