# Self powers
# Problem 48
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000

def solve(problem):
    result = sum( x ** x for x in range(1, problem + 1))
    return str(result)[-10:]

if __name__ == '__main__':
    print(__file__ + ": %s" % solve(1000))
