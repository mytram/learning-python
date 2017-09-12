# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def solve():
    for c in range(1,1000):
        for b in range(1,c):
            for a in range(1,b):
                if a + b + c == 1000 and (a*a + b*b) == c*c:
                    return (a*b*c, a, b, c)

if __name__ == '__main__':
    print(__file__ + ": %d (%d, %d, %d)" % solve())
