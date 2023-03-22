# Project Euler -- Problem 8: Largest Product in a Series
# https://projecteuler.net/problem=8

import time
from numpy import prod # requires numpy to efficiently calculate the product of a list of numbers

start_time = time.time() # to track how long the program takes to run

thousand_digits = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

num_of_digits = 13 # can be changed to any arbitrary number of digits to be checked
saved_digits = [] # to store the adjacent digits that make the greatest product
working_digits = [] # to store the adjacent digits currently being evaluated
working_product = 1 # to store the greatest product of the working_digits

for digit in thousand_digits:
    if len(working_digits) < num_of_digits: 
        #print('Appending', digit)
        working_digits.append(int(digit))
        working_product = prod(working_digits)
        del saved_digits[:] # removes the contest of the list but doesn't replace the old label with a new empty list
        for d in working_digits:
            saved_digits.append(d)
        #print(working_digits, working_product)
        #print('New working_product is', working_product)
        continue
    #print('Appending', digit)
    working_digits.append(int(digit))
    #print(working_digits)
    #print('Deleting', working_digits[0])
    del working_digits[0]
    #print(working_digits)
    if prod(working_digits) > working_product:
        del saved_digits[:] # removes the contest of the list but doesn't replace the old label with a new empty list
        for d in working_digits:
            saved_digits.append(d)
        #print('Saved:', saved_digits)
        #print(prod(working_digits), 'is greater than', working_product)
        working_product = prod(working_digits)
        #print('New working_product is', working_product)

print('The', num_of_digits, 'adjacent digits in that number that have the greatest product are:', saved_digits, '\nTheir product equals:', working_product) # Change the second word to match the number of digits specified in line 16.
print('This program took', time.time() - start_time, 'seconds to run.')
