# http://www.pythonchallenge.com/pc/return/romance.html
# from 4, 13
import base64
import bz2
import cookielib
import httplib2
import re
import xmlrpclib
from urllib2 import HTTPHandler, HTTPCookieProcessor, build_opener, Request
from urlparse import unquote

cookiejar = cookielib.CookieJar()

req = Request("http://www.pythonchallenge.com/pc/def/linkedlist.php")
base64string = base64.b64encode('%s:%s' % ('huge', 'file'))
req.add_header("Authorization", "Basic %s" % base64string)

opener = build_opener(HTTPCookieProcessor(cookiejar), HTTPHandler())
f = opener.open(req)

for cookie in cookiejar:
    print cookie

param = str(12345)
message = ''
while True:
    try:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + param
        r = opener.open(url)
        page_content = r.read()
        print page_content
        data = dict((cookie.name, cookie.value) for cookie in cookiejar)
        message += data['info']
        param = re.findall("busynothing is (\d+)", page_content)[0]

    except IndexError:
        break

print message

res = unquote(message.replace("+", " "))
print(bz2.decompress(res).decode())

server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.phone('Leopold')

http = httplib2.Http()
headers = {'Cookie': 'info=the flowers are on their way'}
response, content = http.request("http://www.pythonchallenge.com/pc/stuff/violin.php", 'GET', headers=headers)
print content
