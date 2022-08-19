from PIL import Image, ImageDraw
from random import randint

hight = 700
width = 500

img = Image.new('RGB', (hight, width), color = (230, 235, 255))

draw = ImageDraw.Draw(img)

n = randint(200, 400)

dots = []

for i in range(n):
    x = randint(0, hight)
    y = randint(0, width)
    dots.append((x, y))

for (x, y) in dots:
    draw.point((x, y), 'black')    

img.save('png.png')