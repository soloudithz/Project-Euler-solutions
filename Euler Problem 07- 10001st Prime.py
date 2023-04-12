# Project Euler -- Problem 7
# https://projecteuler.net/problem=7

import time
start_time = time.time() # to track how long the program takes to run.
solution = 13
count = 6

def is_prime(num):
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True

while count < 10001:
    solution += 2
    if is_prime(solution):
        count += 1        

print(solution, 'is the 10,001st prime.')
print('This program took', time.time() - start_time, 'seconds to run.')
