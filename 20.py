import base64
import re
import urllib2
from urllib2 import Request

next_range = length = 0
content = ''
content_header = None
req = Request("http://www.pythonchallenge.com/pc/hex/unreal.jpg")
base64string = base64.b64encode('%s:%s' % ('butter', 'fly'))
req.add_header("Authorization", "Basic %s" % base64string)

do_loop = True

while do_loop:
    req.headers['Range'] = 'bytes=' + str(next_range) + '-'
    try:
        f = urllib2.urlopen(req)
    except:
        req.headers['Range'] = 'bytes=' + str(length) + '-'
        f = urllib2.urlopen(req)
        do_loop = False
    if f.headers['Content-Type'] != 'image/jpeg':
        content = f.read()
        print content

    content_header = re.search(r'bytes (\d+)-(\d+)/(\d+)', f.headers['Content-Range'])
    next_range, length = int(content_header.group(2)) + 1, int(content_header.group(3)) + 1

print content[::-1]
print 'invader'[::-1]
req.headers['Range'] = 'bytes=' + str(int(content_header.group(1)) - 1) + '-'
f = urllib2.urlopen(req)
print f.read()
req.headers['Range'] = 'bytes=' + str(1152983631) + '-'

f = urllib2.urlopen(req)
with open("21.zip", "wb") as file:
    file.write(f.read())
