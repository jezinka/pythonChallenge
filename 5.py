#http://www.pythonchallenge.com/pc/def/peak.html

import pickle, urllib

url = "http://www.pythonchallenge.com/pc/def/banner.p"
page_content = urllib.urlopen(url).read()

data = pickle.loads(page_content)
for d in data:
    line = []
    for char, quantity in d:
        line += char * quantity
    print "".join(line)
