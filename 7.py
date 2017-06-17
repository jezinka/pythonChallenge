# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

image = Image.open("oxygen.png")
height = image.height / 2
pixel = None
pixels = []

for w in range(0, image.width, 7):
    current_pixel = image.getpixel((w, height))[0]
    pixels.append(current_pixel)

print "".join([chr(pix) for pix in pixels])

print "".join([chr(letter) for letter in [105, 110, 116, 101, 103, 114, 105, 116, 121]])
