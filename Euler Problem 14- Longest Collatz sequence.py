# Project Euler -- Promblem 14: Longest Collatz Sequence
# https://projecteuler.net/problem=14


'''
In 1937, a German mathematician named Lothar Collatz formulated a conjecture
(it still remains unproven) that can be described in the following way:

    1. Take any non-negative and non-zero integer number greater than 1 and name it c0.
    2. If it's even, evaluate a new c0 as c0 ÷ 2.
    3. Otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;

The hypothesis says that regardless of the initial value of c0, it will always go to 1.

The program below reads one natural number and executes the above steps as long as c0
remains different from 1. It also counts the steps needed to achieve the goal.
'''

import time
start_time = time.time()   # to track how long the program takes to run

num_attempted = 1          # The next number to be run through Collatz's sequence
max_attempts = 3000000     # Adjust this number to prevent the program from running indefinitely (unless Collatz was wrong).
max_steps = 0              # Records the greatest number of steps taken to get to 1 from a given starting number, c0
num_causing_max_steps = 0  # Records the initial value that lead to the current max_steps

while num_attempted <= max_attempts:
    steps = 0
    num_attempted += 1
    c0 = num_attempted
    #print('\nInitial value of c0 is ', c0, '\n')
    while c0 != 1:
        steps += 1
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        #print(c0)
    #print('\nFinal value of c0 is ', c0, ' after ', steps, ' steps')
    if steps > max_steps:
        max_steps = steps
        num_causing_max_steps = num_attempted

print('\nThe max number of steps was {output_1:,}, which was produced by the number {output_2:,}.'.format(output_1=max_steps, output_2=num_causing_max_steps))

print('This program took', time.time() - start_time, 'seconds to run.')
