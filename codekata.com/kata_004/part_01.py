# coding: utf-8
#
# weather.dat
# Part One: Weather Data
# In weather.dat you’ll find daily weather data for Morristown, NJ for
# June 2002. Download this text file, then write a program to output
# the day number (column one) with the smallest temperature spread
# (the maximum temperature is the second column, the minimum the third
# column)
#
# data: http://codekata.com/data/04/weather.dat
#
#
import re

def solve():
    with open('weather.dat', 'r') as f:
        lines = [ l for l in f ]
    recs = [l.split() for l in lines[2:-1]]

    for rec in recs:
        for i in range(1,3):
            m = re.match('\A[1-9][0-9]*(\.[0-9]+)?', rec[i])
            if m:
                rec[i] = float(m[0])
            else:
                raise 'data unavailable'

    temp_spreads = [(rec[0], abs(rec[1] - rec[2])) for rec in recs]
    min_spread = min(temp_spreads, key=lambda s: s[1])[1]

    return filter(lambda s: s[1] == min_spread, temp_spreads)

if __name__ == '__main__':
    print("solve: ", tuple(solve()))
