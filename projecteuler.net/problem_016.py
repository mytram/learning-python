# Power digit sum
# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2**1000?

def solve(problem=1000):
    return sum(int(d) for d in str(2 ** problem))

if __name__ == '__main__':
    print(__file__ + ": %s" % solve())
