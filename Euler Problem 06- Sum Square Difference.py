# Project Euler -- Problem 6
# https://projecteuler.net/problem=6

print("For the whole numbers from 1 through 10, the difference between the sum of squares and the square of sums is ", sum(range(1, 101))**2 - sum([i**2 for i in range(1, 101)]), ".", sep="")
