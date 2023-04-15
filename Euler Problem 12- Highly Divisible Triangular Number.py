# Project Euler -- Promblem 12: Highly Divisible Triangular Number
# https://projecteuler.net/problem=12

from functools import reduce
import time

threshold = int(input('The first triangular numbers with at least this many divisors: '))
start_time = time.time() # to track how long the program takes to run.

def infinite_triangular():
    num = 1
    triangle = 1
    while True:
        yield triangle
        num += 1
        triangle += num

def factors_of(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

triangle = infinite_triangular()
check = next(triangle)
while len(factors_of(check)) <= threshold:
    #print(check) # in case you're curious...
    check = next(triangle)
print('...is {output:,}.'.format(output=check),
      'It has {output:,} divisors.'.format(output=len(factors_of(check))))
print('This program took', time.time() - start_time, 'seconds to run.')
