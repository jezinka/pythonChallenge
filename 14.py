# http://www.pythonchallenge.com/pc/return/italy.html
import math
from PIL import Image

one_line = Image.open("wire.png")
source_width = one_line.width
sqrt = int(math.sqrt(source_width))
image = Image.new('RGB', (sqrt, sqrt))

width = range(0, sqrt)
height = range(0, sqrt)

pix_xy = 0

while pix_xy < source_width:

    for i in width:
        pixel = one_line.getpixel((pix_xy, 0))
        image.putpixel((i, height[0]), pixel)
        pix_xy += 1
    height = height[1::]

    for j in height:
        pixel = one_line.getpixel((pix_xy, 0))
        image.putpixel((width[-1], j), pixel)
        pix_xy += 1
    width = width[0:-1]

    for k in width[::-1]:
        pixel = one_line.getpixel((pix_xy, 0))
        image.putpixel((k, height[-1]), pixel)
        pix_xy += 1
    height = height[0:-1]

    for l in height[::-1]:
        pixel = one_line.getpixel((pix_xy, 0))
        image.putpixel((width[0], l), pixel)
        pix_xy += 1
    width = width[1::]

image.show()
