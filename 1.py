# http://www.pythonchallenge.com/pc/def/map.html

import string
from numpy import roll

letters = string.lowercase
transition = ''.join(roll(list(letters), -2))

trans = string.maketrans(letters, transition)

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print text.translate(trans)
print 'map'.translate(trans)