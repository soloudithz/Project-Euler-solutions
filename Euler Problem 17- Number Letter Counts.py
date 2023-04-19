# Project Euler -- Promblem 17: Number Letter Counts
# https://projecteuler.net/problem=17

from num2words import num2words
import time

n = int(input('The sum of all letters in all numbers up to (and including) '))

start_time = time.time()   # to track how long the program takes to run

string_of_nums = ''

for i in range(1, n+1):
    string_of_nums += num2words(i)
for character in ('-', ' '):
    string_of_nums = string_of_nums.replace(character, '')
#print(string_of_nums)

print('is {output:,}.'.format(output=len(string_of_nums)))
print('This program took', time.time() - start_time, 'seconds to run.')
