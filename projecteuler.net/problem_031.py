# coding: utf-8
#
# Coin sums
# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


# @TODO: Use a generator version to get rid of recursions
def find_combinations(numbers, total):
    head, *tail = numbers
    max_qty = total // head

    combinations = []
    if len(tail) == 0:
        for qty in range(0, max_qty + 1):
            if head * qty == total:
                combinations.append([(head, qty, head * qty)])
        return combinations

    for qty in range(0, max_qty + 1):
        head_total = head * qty
        sub_total = total - head_total
        sub_combinations = find_combinations(tail, sub_total)
        for sub in sub_combinations:
            if sum(t[2] for t in sub) + head * qty == total:
                combinations.append([(head, qty, head * qty), *sub])

    return combinations

def gen_combinations(numbers, total):
    #
    # initial_total
    sub_total = total
    tail = numbers

    while True:
        head, *tail = tail
        max_qty = sub_total // head

        combinations = []
        if len(tail) == 0:
            for qty in range(0, max_qty + 1):
                if head * qty == sub_total:
                    combinations.append([(head, qty, head * qty)])
                return combinations

        for qty in range(0, max_qty + 1):
            head_total = head * qty
            sub_total = total - head_total
            sub_combinations = find_combinations(tail, sub_total)
            for sub in sub_combinations:
                if sum(t[2] for t in sub) + head * qty == total:
                    combinations.append([(head, qty, head * qty), *sub])

        return combinations

def solve(problem):
    coin_set = [1, 2, 5, 10, 20, 50, 100, 200]
    combinations = find_combinations(coin_set, problem)
    # print("com: "  + str(combinations))
    return len(combinations)

if __name__ == '__main__':
    print(__file__ + ": %d" % solve(200))
