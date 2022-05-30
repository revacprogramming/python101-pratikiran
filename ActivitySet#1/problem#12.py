# Regular Expressions
# https://www.py4e.com/lessons/regex

import re

x = "dataset/regex_sum_42.txt"
z = "dataset/regex_sum_1548409.txt"

sum = 0

f = open(z)
for line in f:
    i = re.findall("[0-9]+", line)
    if i != []:
        for j in i:
            sum += int(j)

print(sum)