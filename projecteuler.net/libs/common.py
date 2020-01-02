# For finding all the small primes, say all those less than
# 10,000,000,000; one of the most efficient ways is by using the Sieve
# of Eratosthenes (ca 240 BC):
#
# Make a list of all the integers less than or equal to n (greater
# than one) and strike out the multiples of all primes less than or
# equal to the square root of n, then the numbers that are left are
# the primes. (See also our glossary page.)

import math

def lst_to_int(ds):
    number = 0
    for d in ds:
        number = number * 10 + d
    return number

def is_prime(num):
    """
Returns True if num is a prime number, otherwise False.
Note: Generally, isPrime() is slower than prime Sieve().
all numbers less than 2 are not prime
"""
    if num < 2:
        return False
    # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

class FactorialGenerator:
    def __init__(self):
        self._series = [1]
        self._index = 0

    def __iter(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index == len(self._series):
            self._series.append(self._series[-1] * (self._index + 1))
        self._index += 1
        return self._series[self._index - 1]

    @property
    def number(self):
        return self._index + 1

    def get(self, f):
        if f <= 0:
             return 0
        # thread unsafe
        index = f - 1
        nf = len(self._series)
        while index >= nf:
            self._series.append(self._series[-1] * (nf + 1))
            nf += 1
        return self._series[index]

class PrimeGenerator:
    def __init__(self, lt = None, gen_step = 1_000):
        self._lt = lt
        self._index = 0
        self._prime_series = []

        bound = self._lt
        if bound == None: bound = 1_000

        self._current_bound = 2
        self.generate_primes(bound)

    @property
    def lt(self): return self._lt

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self.lt != None and self.lt < 2: raise StopIteration
        if self._index == len(self._prime_series):
            #
            # Stop if a less than limit is set
            #
            if self._lt != None:
                raise StopIteration
            else:
                # Generate 1_000 more otherwise
                self.generate_primes(self._current_bound + 1_000)

        prime = self._prime_series[self._index]
        if self.lt != None and prime >= self.lt: raise StopIteration
        self._index += 1

        return prime

    #
    # @TODO: Simplify this
    #
    def generate_primes(self, bound):
        stop = math.sqrt(bound)
        numbers = range(self._current_bound, bound)

        for next_prime in self._prime_series:
            if next_prime >= stop: break
            numbers = tuple(x for x in numbers if x % next_prime != 0)

        if len(numbers) > 0:
            self._prime_series.append(numbers[0])

        next_prime = self._prime_series[-1]

        while len(numbers) > 1 and next_prime < stop:
            numbers = tuple(x for x in numbers if x % next_prime != 0)
            self._prime_series.append(numbers[0])
            next_prime = numbers[0]

        self._prime_series = sorted(list(set(self._prime_series) | set(numbers)))
        self._current_bound = bound

#
#
# Taken from the forum
#
def calculate_prime_factors(n):
    result = []
    d = 2
    while d * d <= n:
       if n % d == 0:
           result.append(d)
           n //= d
       else:
           d += 1
    if n > 1:
       result.append(n)
    return result
