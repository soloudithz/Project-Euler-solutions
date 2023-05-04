# Project Euler -- Promblem 22: Name Scores
# https://projecteuler.net/problem=22

# For benchmarking purposes, this version of the code contains a solution found at: 
# https://blog.dreamshire.com/solutions/project_euler/project-euler-problem-022-solution/
# ..., which is a fantastic blog featuring concise solutions to the Project Euler problems.

import time

# Read in data. Then clean it up by removing the quotation marks, splitting it into a
# lists of names (as strings) by splitting at commas, and then sorting it alphabetically. 
with open("pe022_names.txt", "r") as file:
    names = list(file.read().replace('"', "").split(","))
names = sorted(names)
name_scores = []    # To store individual name scores; handy for printing, if needed

start_time = time.time() # to track how long the program takes to run.

# Dreamshire approach to solving this problem
score = lambda word: sum(ord(c)-64 for c in word)
names = sorted(open('pe022_names.txt').readline()[1:-1].split('","'))
s = sum(ln*score(name) for ln, name in enumerate(names, 1))
print ("Total name score =", s)

# Timing code
print('This program took', time.time() - start_time, 'seconds to run.')
