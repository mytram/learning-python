# coding: utf-8

# Part Two: Soccer League Table
# The file football.dat contains the results from the English Premier
# League for 2001/2. The columns labeled ‘F’ and ‘A’ contain the total
# number of goals scored for and against each team in that season (so
# Arsenal scored 79 goals against opponents, and had 36 goals scored
# against them). Write a program to print the name of the team with
# the smallest difference in ‘for’ and ‘against’ goals.

import re
def find_for_and_against_differences():
    with open('football.dat', 'r') as f:
        lines = f.readlines()

    club_records = [ line.split() for line in lines[1:] if not re.match('\A\s+-+', line) ]

    for rec in club_records:
        m = re.match('[0-9]+', rec[6])
        rec[6] = int(m[0])
        m = re.match('[0-9]+', rec[8])
        rec[8] = int(m[0])

    return [(rec[1], abs(rec[6] - rec[8])) for rec in club_records]


def solve():
    diffs = find_for_and_against_differences()
    smallest_diff = min(diffs, key=lambda n: n[1])[1]
    return filter(lambda diff: diff[1] == smallest_diff, diffs)

if __name__ == '__main__':
    print("the team with the smallest difference: ", tuple(diff[0] for diff in solve()))
