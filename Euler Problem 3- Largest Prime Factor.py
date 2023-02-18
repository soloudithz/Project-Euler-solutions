# This is not my solution but is the fastest one
# that I have found for numbers less than 10^21.
# https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-003-solution/

# In the interest of learning, I have added some annotations to the solution code to help
# myself and others understand how this algorithm works.

n = int(input('The largest prime factor of '))
start = time.time()
while n%2==0: n//= 2  # Remove all even factors
d = 3
while d*d <= n:
    if n % d == 0:
        n//= d
    else:
        d+= 2
print ("is", 2 if n==1 else n)
