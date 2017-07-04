import binascii
import difflib
import gzip
import io
import re
from PIL import Image

column_1, column_2 = [], []

for line in gzip.open("deltas.gz"):
    match = re.match(r'([0-9a-f ]*) {3}([0-9a-f ]*)\n', line)
    column_1.append(match.group(1))
    column_2.append(match.group(2))

bytes_1, bytes_2, bytes_3 = '', '', ''
difference = difflib.Differ().compare(column_1, column_2)
for line in list(difference):
    data_only = ''.join(line[2:].strip().split(' '))
    if data_only:
        ind = line[0]
        if ind == "+":
            bytes_1 += data_only
        elif ind == "-":
            bytes_2 += data_only
        else:
            bytes_3 += data_only

for data in [bytes_1, bytes_2, bytes_3]:
    stream = io.BytesIO(binascii.unhexlify(data))
    img = Image.open(stream)
    img.show()
