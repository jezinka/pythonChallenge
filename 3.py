import re

f = open('3.txt', 'r')

print "".join(re.findall(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", f.read()))