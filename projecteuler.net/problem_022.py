# # coding: utf-8

# Names scores
# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

def solve():
    with open('p022_names.txt', 'r') as f:
        names = ''.join(f.readlines())
    names = sorted(
        names.strip().replace('"', '').split(',')
    )
    base = ord('A') - 1
    return sum(
        sum(
            ord(x) - base for x in name
        ) * (index + 1) for index, name in enumerate(names)
    )

if __name__ == '__main__':
    print(__file__ + ": %d" % solve())