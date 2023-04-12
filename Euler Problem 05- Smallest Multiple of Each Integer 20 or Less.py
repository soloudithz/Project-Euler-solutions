# Project Euler -- Problem 5
# https://projecteuler.net/problem=5

from math import lcm

x = list(range(1, int(input("Find LCM of numbers 1 through: "))+1))
print(lcm(*x)) # the asterisk unpacks list x, because lcm() cannot operate on a list


'''
EXPLANATION:
Python 3.9's math module provides built-in functionality to calculate the least common
multiple (LCM) of an arbitrary group of whole numbers. So, we can simply create a list
of the numbers in range of positive whole numbers from 1 through an arbitrary number.
This is a fast, Pythonic way to solve the problem. At the bottom of this script, I have
provided another, inefficient way to calculate the LCM. That script is based on a
method of calculation found on the Wikipedia page for least common multiple found at:
https://en.wikipedia.org/wiki/Least_common_multiple, as accessed on March 15, 2023. This
code currently implements the "simple algorithm" method found on that page.

Using a simple algorithm:
The following code lists a set of postive integers ranging from 1 through the selected
number. During each pass of the algorithm, the least element is incremented by its
corresponding initial value. If using a sequential set of numbers, simply run the program
as is. If you want to put in an arbitrary set of numbers, un-comment the commented
variables and vice versa, and do the same with the first two lines of the while loop below.
Note that this is an inefficient method that becomes to slow with max numbers above 16.


x = list(range(1, int(input("Find LCM of numbers 1 through: "))+1))
#x = list(input("Find the LCM of the folrlowing numbers (separated by spaces):").split())
#x = [int(i) for i in x]
#y = [num for num in x]

print("Running...")
while min(x) != max(x):
    x[x.index(min(x))] += x.index(min(x)) + 1
    #x[x.index(min(x))] += y[x.index(min(x))]
print("The LCM is", max(x))
'''
