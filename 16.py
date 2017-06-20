# http://www.pythonchallenge.com/pc/return/mozart.html
from PIL import Image
from numpy import roll

image = Image.open("mozart.gif")
new_image = Image.new('RGB', image.size)
pixels = image.load()

# first_row = [pixels[w, 0] for w in range(image.width)]  # 5 * pix->195

for h in range(image.height):
    row = [pixels[w, h] for w in range(image.width)]
    indicator_idx = row.index(195)
    rolled_row = roll(row, -indicator_idx)
    for w in range(image.width):
        new_image.putpixel((w, h), rolled_row[w])

new_image.show()
