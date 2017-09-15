# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

month_days = {
    31: [1, 3, 5, 7, 8, 10, 12],
    30: [4, 6, 9, 11]
}

def is_leap_year(year):
    return (year % 4 == 0 and year % 100) or (year % 400 == 0)

def add_1_month(year, month, day, day_of_week):
    yield(year, month, day, day_of_week)

    while True:
        if month in month_days[31]:
            day_of_week += 31
        elif month in month_days[30]:
            day_of_week += 30
        elif is_leap_year(year):
            day_of_week += 29
        else:
            day_of_week += 28

        day_of_week %= 7

        month += 1
        if month == 13:
            month = 1
            year += 1

        yield(year, month, day, day_of_week)

def solve():
    date = (1900, 1, 1, 1) # first day

    day_1_of_month = add_1_month(*date)

    count = 0
    for year, month, day, day_of_week in day_1_of_month:
        if year == 1900: continue
        if year > 2000: return count
        if day_of_week == 0:
            count += 1

if __name__ == '__main__':
    print(__file__ + ": %s" % solve())
