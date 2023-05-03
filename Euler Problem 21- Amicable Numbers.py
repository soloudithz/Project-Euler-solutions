# Project Euler -- Promblem 18: Maximum Path Sum I
# https://projecteuler.net/problem=21

import time
start_time = time.time() # to track how long the program takes to run.

amicable_nums = []
check_num = 0
subtotals = []
sum_of_amicable_nums = 0

def factors_of(n):
    factors = []
    for i in range(1, n+1):
        if (n) % i == 0:
            factors.append(i)
        #print("Factors of", i, "are:", factors)
    return factors


def proper_divisors_of(n):
    pd = factors_of(n)
    #print("pd:", pd)
    del pd[-1]
    #print("pd:", pd)
    return pd


n = int(input("Find amicable numbers to: "))

for i in range(2, n+1):
    #print("i: ", i)
    check_num = sum(proper_divisors_of(i))
    #print("check_num: ", check_num)
    if i != check_num:
        if ((i, check_num) not in amicable_nums) and ((check_num, i) not in amicable_nums):
            if sum(proper_divisors_of(check_num)) == i:
                #print(i, "and", check_num, "are amicable numbers!")
                amicable_nums.append((i, check_num))
for i in amicable_nums:
    subtotals.append(sum(i))
sum_of_amicable_nums = sum(subtotals)

print("The sum of all the amicable numbers under {output:,} ".format(output=n) + "is {output:,}.".format(output=sum_of_amicable_nums))
print('This program took', time.time() - start_time, 'seconds to run.')

#print("Amicable numbers:", amicable_nums)
#print("Subtotals of amicable pairs:", subtotals)