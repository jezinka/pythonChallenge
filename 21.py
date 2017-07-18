import bz2
import zlib
from zipfile import ZipFile

zip_file = ZipFile('21.zip', 'r')

for info in zip_file.infolist():
    filename = info.filename
    print filename
    if 'txt' in filename:
        print zip_file.open(filename, pwd='redavni').read()
    else:
        zip_file.extract(member=filename, pwd='redavni')
        print 'extracted'

result = ''
data = open('package.pack').read()

while True:
    if data.startswith(b'x\x9c'):
        data = zlib.decompress(data)
        result += '.'
    elif data.startswith(b'BZh'):
        data = bz2.decompress(data)
        result += '*'
    elif data.endswith(b'\x9cx'):
        data = data[::-1]
        result += '\n'
    else:
        break

print(data[::-1])
print result
