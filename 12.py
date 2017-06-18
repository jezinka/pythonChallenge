# http://www.pythonchallenge.com/pc/return/evil.html
import os
import urllib

print urllib.urlopen(
    "http://huge:file@www.pythonchallenge.com/pc/return/evil4.jpg?username=huge&password=file").readline()

if not os.path.exists('images'):
    os.makedirs('images')

data = open("evil2.gfx", "rb").read()
for i in range(5):
    for extension in ['png', 'jpg', 'gif']:
        open('images/%d.' % i + extension, 'wb').write(data[i::5])
