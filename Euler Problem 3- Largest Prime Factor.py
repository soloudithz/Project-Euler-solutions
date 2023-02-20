# This is not my solution but is the fastest one
# that I have found for numbers less than 10^21.
# https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-003-solution/

# In the interest of learning, I have added some
# annotations to the solution code to help myself
# and others understand how this algorithm works.

# Explanation: Due to the commutative property of
# multiplication, you can rearrange all the prime
# factors (of a given number) in any order and can
# therefore factor a number in a systematic way, 
# from least to greatest. One consequence of this
# is that once all factors of a given value have
# factored out of the starting number, you don't 
# need to check them again. In other words, once 
# all 2s are factored out, you can move on to 3s
# and so on. So, this algorithm factors out 2s,
# then 3s, then all odd numbers after 3 (because
# all evens are just multiples of 2. There is some
# wasted overhead in checking multiples of odd 
# numbers, the first example being 9, which is
# the first multiple of 3 that isn't also a
# multiple of 2 and, therefore, already skipped.
# But, because this algorithm only uses two 
# variable (i.e., it doesn't make lists of
# prime factors or numbers checked) it is very
# efficient, only returning the last factor, n,
# which is the largest prime factor of the
# starting number (also n). 

n = int(input('The largest prime factor of '))
while n%2==0: n//= 2  # Remove all even factors.
d = 3
while d*d <= n:  # Don't check a number if it's first unchecked multiple (it's square) is greater than n. 
    if n % d == 0:
        n//= d  # Floor division prevents unnecessary decimals
    else:
        d+= 2  # Skip to the next odd number.
print ("is", 2 if n==1 else n)
