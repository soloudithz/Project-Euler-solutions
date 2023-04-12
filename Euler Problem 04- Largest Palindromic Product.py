#Find the largest palindrome made from the product of two 3-digit numbers
#Range of numbers to check is 10,000 through 998,001, because that is the
#range from 100 x 100 through 999 x 999.

#Variables to customize the range.
#Warning: This brute-force method only runs quickly for 3-digit numbers.
#It runs moderately with 4-digit ranges and slowly beyond that.
l = 100 #lower bound
u = 999 + 1 #upper bound

print("The largest palindrome between 100x100 and 999x999 is", max(a*b for a in range(l, u) for b in range(l, u) if str(a*b)==str(a*b)[::-1]))
#print(list(a*b for a in range(l, u) for b in range(l, u) if str(a*b)==str(a*b)[::-1]))
print("In that range, there are", len(list(a*b for a in range(l, u) for b in range(l, u) if str(a*b)==str(a*b)[::-1])), "palindromic multiples of 3-digit numbers.")
