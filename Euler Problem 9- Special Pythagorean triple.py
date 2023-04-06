# This solution is adapted from a an excellent and well-explained solution found at:
# https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-009-solution/
# Their answer remains intact. I have adjusted for readability upon output and proof that
# the numbers fit Pythagoras' theorem. My comments below summarize the code for learners.

n = int(input("The Pythagorean triplet that sums to ")) # Asks user for the target number that a + b + c sums to.
p = -1; trip = "None."                                  # Set p to -1. This prints if no triples are found summing to n.
for a in range(n//3-1, 2, -1):                          # See comment at end for the explanation of the following lines.
    b = n*(n-2*a) // (2*(n-a))
    c = n - a - b
    if a<b and a*a + b*b == c*c:                        # Checking a<b before the Pythagorean theorem is faster. Checking b<c is implied.
        p = a*b*c
        trip=(a,b,c)
        break
print("is", trip, "\n")                                 # Prints answer. In cases with multiple correct answers, it prints the greatest.
print("To show that this is actually a Pythagorean triple:")
print(trip[0], "squared, plus", trip[1], "squared, equals",
      trip[2], "squared. Or...")
print(trip[0]**2, "+", trip[1]**2, "=", trip[2]**2)


'''
For lines 8 through 10:
Looking downward from n//3, the first product (p) meeting the conditional’s criteria will
be our maximum and we can break from the loop. If no solution is found then the value of
p is −1. Here’s the justification for using n//3:
    given: n = a+b+c
    given: a<b<c
    infer: a<b, b<c
    add the two equations: 2a < b+c
    add a to both sides: 3a <  a+b+c
    replace a + b + c with the equivalent n: 3a < n
    therefore: a < n//3
'''
