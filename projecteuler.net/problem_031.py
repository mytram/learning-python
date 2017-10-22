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
def find_combinations(coins, total):
    head, *tail = coins
    max_qty = total // head

    combinations = []

    for qty in range(0, max_qty + 1):
        head_total = head * qty
        if len(tail) == 0:
            if head_total == total:
                combinations.append([head])
        else:
            for sub in find_combinations(tail, total - head_total):
                combinations.append([head, *sub])

    return combinations

def solve(problem):
    coin_set = [1, 2, 5, 10, 20, 50, 100, 200]
    combinations = find_combinations(coin_set, problem)
    return len(combinations)

if __name__ == '__main__':
    print(__file__ + ": %d" % solve(200))
