from PIL import Image

image = Image.open("cave.jpg")
h = image.height
w = image.width
even = Image.new('RGB', (w, h))
odd = Image.new('RGB', (w, h))

for x in range(w):
    for y in range(h):
        pixel = image.getpixel((x, y))
        if (x + y) % 2 == 0:
            even.putpixel((x, y), pixel)
        else:
            odd.putpixel((x, y), pixel)

even.show()
odd.show()
