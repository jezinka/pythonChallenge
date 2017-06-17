# http://www.pythonchallenge.com/pc/def/channel.html
from zipfile import ZipFile
import re

archive = ZipFile('channel.zip')
readme = archive.read('readme.txt')
print readme

filename = re.findall("start from (\d+)", readme)[0]
comments = []
while(True):
    file = archive.read(filename + '.txt')
    comments += archive.getinfo(filename + '.txt').comment
    print file
    try:
        filename = re.findall("nothing is (\d+)", file)[0]
    except:
        break

print "".join(comments)

