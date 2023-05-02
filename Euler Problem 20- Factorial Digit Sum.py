# Project Euler -- Promblem 20: Factorial Digit Sum
# https://projecteuler.net/problem=20

from math import factorial as f

f_digit_sum = 0
for digit in str(f(int(input("The sum of digits for the factorial of ")))):
    f_digit_sum += int(digit)
print("is {output:,}.".format(output=f_digit_sum))