# Project Euler -- Problem 7
# https://projecteuler.net/problem=7

import time
start_time = time.time() # to track how long the program takes to run.
solution = 13
count = 6
#list_of_primes = [2, 3, 5, 7, 11, 13]

def is_prime(num):
    #for prime in list_of_primes:
        #if prime **2 <= num:
            #if num % prime == 0:
                #print(num, ' is divisible by ', prime, '.', sep='')
                #return False
    for i in range(3, num, 2):
        if num % i == 0:
            #print(num, ' is divisible by ', i, '.', sep='')
            return False
    #list_of_primes.append(num)
    #print(str(num), 'is prime.')
    #print(list_of_primes)
    return True

while count < 10001:
    solution += 2
    if is_prime(solution):
        count += 1        

print(solution, 'is the 10,001st prime.')
print('This program took', time.time() - start_time, 'seconds to run.')
