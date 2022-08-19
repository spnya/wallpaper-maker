from PIL import Image, ImageDraw
from random import randint

width = 1980
hight = 1080

img = Image.new('RGB', (width, hight), color = (230, 235, 255))

draw = ImageDraw.Draw(img)

n = 30

dots = []

for i in range(n):
    x = randint(0, width)
    y = randint(0, hight)
    dots.append({
        'x': x,
        'y': y,
        'links': []
    })

for i in dots:
    draw.point((i['x'], i['y']), 'black')    

for i in dots:
    for j in dots:
        if (randint(1, 4) == 1):
            draw.line((i['x'], i['y'], j['x'], j['y']), fill=1)

img.save('./images/img1.png')