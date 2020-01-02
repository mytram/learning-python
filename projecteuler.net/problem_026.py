"""projecteuler problem026"""

class Problem026:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator
        self._division_steps = []
        self._recurring_decimal_points = tuple()
        self._call()

    def __str__(self):
        if self.is_recurring:
            return f'{self.nominator}/{self.denominator} {self.recurring_decimal_points} {len(self.recurring_decimal_points)}'
        else:
            return f'{self.nominator}/{self.denominator}'

    @property
    def is_recurring(self):
        return self._recurring_decimal_points is not None

    @property
    def recurring_decimal_points(self):
        return self._recurring_decimal_points

    def _call(self):
        nominator = self.nominator
        denominator = self.denominator

        while True:
            if self._has_seen_divisor(nominator):
                self._assign_recurring_decimal_points(nominator)
                return

            quotient = nominator // denominator
            remainder = nominator % denominator

            self._division_steps.append((nominator, quotient))

            if remainder == 0:
                return

            nominator = remainder * 10

    def _has_seen_divisor(self, divisor):
        for seen, _ in self._division_steps:
            if seen == divisor:
                return True
        return False

    def _assign_recurring_decimal_points(self, nominator):
        pos = self._find_index_of_recurring_divisor(nominator)

        self._recurring_decimal_points = tuple(
            decimal_point for _, decimal_point in self._division_steps[pos:]
        )

    def _find_index_of_recurring_divisor(self, divisor):
        return next(i for i, (d, _) in enumerate(self._division_steps) if d == divisor)

if __name__ == '__main__':
    decimal_reprs = tuple(Problem026(1, denom) for denom in range(1, 1001))
    result = max(decimal_reprs, key=lambda a: len(a.recurring_decimal_points))
    print(result.denominator)
