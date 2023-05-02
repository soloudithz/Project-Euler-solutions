# Project Euler -- Promblem 18: Maximum Path Sum I
# https://projecteuler.net/problem=18


triangle_of_nums = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# Clean up data by converting to a list of strings by splitting at newlines
# and then making each list item its own sub-list by splitting at spaces.
triangle_of_nums = triangle_of_nums.split('\n')
triangle_of_nums = [i.split(' ') for i in triangle_of_nums]

solution = triangle_of_nums[:] # Copy the original list.

# Starting at the next-to-last row, increment each number by the max() of the two adjacent
# numbers below.
for row_idx in range(len(solution)-2, -1, -1):
    for col_idx in range(len(solution[row_idx])):
        left = int(solution[row_idx+1][col_idx])
        right = int(solution[row_idx+1][col_idx+1])
        solution[row_idx][col_idx] = int(solution[row_idx][col_idx]) + max(left, right)
print("The maximum total from top to bottom is {output:,}.".format(output=solution[0][0]))


# Alternatively, you can save the data as a .txt file and read it in line by line, as is 
# shown in the solution below. Alternative solution found at: 
# https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-018-solution/
"""
table = [list(map(int, s.split())) for s in open('pe18.txt').readlines()]

for row in range(len(table)-1, 0, -1):
    for col in range(0, row):
        table[row-1][col]+= max(table[row][col], table[row][col+1])

print ("Maximum top-bottom total in triangle", table[0][0])
"""