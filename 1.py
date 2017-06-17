# http://www.pythonchallenge.com/pc/def/map.html

import string
letters = string.lowercase
trans = string.maketrans(letters, letters[2::] + letters[0:2])

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print text.translate(trans)
print 'map'.translate(trans)