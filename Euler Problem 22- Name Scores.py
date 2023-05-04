# Project Euler -- Promblem 22: Name Scores
# https://projecteuler.net/problem=22

import string
import time

start_time = time.time() # to track how long the program takes to run.


# Read in data. Then clean it up by removing the quotation marks, splitting it into a
# lists of names (as strings) by splitting at commas, and then sorting it alphabetically. 
with open("pe022_names.txt", "r") as file:
    names = list(file.read().replace('"', "").split(","))
names = sorted(names)
name_scores = []    # To store individual name scores; handy for printing, if needed

# Make a dictionary with letter values {"A": 1, "B": 2, ..., "Z": 26}
value_of = {}
letters = string.ascii_uppercase
letters = list(letters)
for i in range(len(letters)):
    value_of[letters[i]] = i+1

for i in range(1, len(names)+1):
    score = 0
    for letter in names[i-1]:
        #print(letter)
        score += value_of[letter.upper()]
    #print(names[i], "has a score of", (score))
    #print("... and a name score of:", str(i), "*", str(score), "=", str(i * score))
    name_scores.append(i * score)

print("The total of all the name scores is {output:,}.".format(output=sum(name_scores)))

print('This program took', time.time() - start_time, 'seconds to run.')