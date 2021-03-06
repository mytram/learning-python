# Even Fibonacci numbers
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms
# will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.

def fib(n):
    if n < 0: return 0
    if n < 3: return n
    fn_2, fn_1 = 1, 2 # f(n-1), f(n-1)
    for n in range(3, n+1):
        fn_2, fn_1 = fn_1, fn_2 + fn_1
    return fn_1

def fib_series(upto):
    if upto < 1: return
    yield 1
    if upto < 2: return
    yield 2
    fn_1, fn = 2, 3
    while fn < upto:
        yield fn
        fn_1, fn = fn, fn_1 + fn

def solve(max_fib = 4_000_000):
    return sum(filter(lambda f: f % 2 == 0, fib_series(max_fib)))

if __name__ == '__main__':
    print(__file__ + ": %s" % solve())
