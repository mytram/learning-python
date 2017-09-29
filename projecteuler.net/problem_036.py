# Double-base palindromes
# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_double_base_palindromic(x):
    as_str = str(x)
    b2 = '{0:b}'.format(x)
    return as_str == ''.join(reversed(as_str))  and b2 == ''.join(reversed(b2))

def double_base_palindromes():
    n = 1
    while True:
        if is_double_base_palindromic(n):
            yield n
        n += 1

def solve():
    palindromes = double_base_palindromes()
    palindrome = next(palindromes)
    total = 0
    while palindrome < 1_000_000:
        total += palindrome
        palindrome = next(palindromes)
    return total

if __name__ == '__main__':
    print(__file__ + ': ', solve())
