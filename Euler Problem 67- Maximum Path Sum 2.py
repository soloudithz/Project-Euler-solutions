# Project Euler -- Promblem 18: Maximum Path Sum I
# https://projecteuler.net/problem=67

# Note: Refer to Project Euler Problem #18 and my solution for mor information. They can be found at:
# https://github.com/soloudithz/Project-Euler-solutions


# Read in data line by line. Then convert it to a list of lists of strings by splitting at newlines
# and making each list item its own sub-list by splitting at spaces.
triangle_of_nums = [list(map(int, s.split())) for s in open('pe067_triangle.txt').readlines()]
solution = triangle_of_nums[:] # Copy the original list.

# Starting at the next-to-last row, increment each number by the max() of the two adjacent
# numbers below.
for row_idx in range(len(solution)-2, -1, -1):
    for col_idx in range(len(solution[row_idx])):
        left = int(solution[row_idx+1][col_idx])
        right = int(solution[row_idx+1][col_idx+1])
        solution[row_idx][col_idx] = int(solution[row_idx][col_idx]) + max(left, right)
print("The maximum total from top to bottom is {output:,}.".format(output=solution[0][0]))