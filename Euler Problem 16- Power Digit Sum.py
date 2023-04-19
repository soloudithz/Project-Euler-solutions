# Project Euler -- Promblem 16: Power Digit Sum
# https://projecteuler.net/problem=16

import time

x = int(input('The power-digit sum of the number: '))
n = int(input('raised to the power of: '))

start_time = time.time()   # to track how long the program takes to run

product = str(x**n)
power_digit_sum = 0
#print(product)
#print('len(product):', len(product))

for digit in product:
    power_digit_sum += int(digit)
    #print('digit:', digit)
    #print('sum:', power_digit_sum)

print('is {output:,}'.format(output=power_digit_sum))
print('This program took', time.time() - start_time, 'seconds to run.')
