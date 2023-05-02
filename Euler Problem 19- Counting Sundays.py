# Project Euler -- Promblem 19: Counting Sundays
# https://projecteuler.net/problem=19

import datetime as dt

count_sundays = 0

for year in list(range(1901, 2001)):        # List each year in the twentieth century. For each year...
    for month in range(1, 13):
        first_of_month = dt.datetime(year, month, 1)
        if first_of_month.weekday() == 6:   # ... if the first day of the month is a Sunday, ...
            count_sundays += 1              # increment the number of Sundays by 1.
print(str(count_sundays) + " Sundays fell on the first of the month in the twentieth century.")