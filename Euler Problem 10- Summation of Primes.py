# Project Euler -- Problem 10: Summation of Primes
# https://projecteuler.net/problem=10

# Algorithm based on explanation and pseudocode found at:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import time
n = int(input("The sum of prime numbers below "))

start_time = time.time() # to track how long the program takes to run.

numbers = [i for i in range(n)]
sieve = [True for n in range(n)]
sieve[0] = False
sieve[1] = False

for n in numbers:
    if n*n > len(numbers): # test later with max()
        break
    if sieve[n] is True:
        for j in range(n*n, len(numbers), n):
            sieve[j] = False

print('is {output:,}.'.format(output = sum(list(n for n in numbers if sieve[n] is True))))

print('This program took', time.time() - start_time, 'seconds to run.')
