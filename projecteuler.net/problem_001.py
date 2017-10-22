# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_3_or_5(below):
    i = 3

    while i < below:
        if i % 3 == 0 or i % 5 == 0:
            yield i
        i += 1

def solve():
    return sum(multiples_of_3_or_5(1000))

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
