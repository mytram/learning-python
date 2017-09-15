# coding: utf-8

# Integer right triangles
# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

import math
def find_solutions_for_perimeter(perimeter):
    end = perimeter + 1
    for a in range(1, end):
        for b in range(1, end):
            c2 = a * a + b * b
            c = int(math.sqrt(c2))
            p = a + b + c
            if p > perimeter: break
            if c2 == c*c:
                yield (c, p)

def solve():
    solution_count = {}
    g = find_solutions_for_perimeter(1000)
    max = 0
    solution = 0
    for s in g:
        perimeter = s[1]
        solution_count[perimeter] = solution_count.get(perimeter, 0) + 1
        if solution_count[perimeter] > max:
            max = solution_count[perimeter]
            solution = perimeter
    return solution

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())
