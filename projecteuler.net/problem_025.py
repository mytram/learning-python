# coding: utf-8

# 1000-digit Fibonacci number
# Problem 25
# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fib():
    yield 1
    yield 1
    fn_2, fn_1 = 1, 1 # f(n-1), f(n-1)

    while True:
        fn_2, fn_1 = fn_1, fn_2 + fn_1
        yield fn_1

def solve():
    f = fib()
    n = next(f)
    i = 1
    while len(str(n)) < 1000:
        n = next(f)
        i += 1
    return i

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
