# Regular Expressions
# https://www.py4e.com/lessons/regex

import re

f = open("dataset/romeo.txt", "r")
x = re.search("^It.*sun$", f)
print(f.read())