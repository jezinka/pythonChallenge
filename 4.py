# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib, re

param = str(12345)
status = 200

while(True):
    try:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + param
        page_content = urllib.urlopen(url).read()
        print page_content
        param = re.findall("nothing is (\d+)", page_content)[0]
    except IndexError:
        if page_content.endswith('.html'):
            break
        param = str(int(param)/2)

