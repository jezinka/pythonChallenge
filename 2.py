# http://www.pythonchallenge.com/pc/def/ocr.html
import re

f = open('2.txt', 'r')
histogram = {}
file = f.read()

for char in file:
    if char != '\n':
        if char in histogram.keys():
            histogram[char] += 1
        else:
            histogram[char] = 1

print histogram

print re.findall(r"[a-z]", file)