from PIL import Image, ImageDraw
from random import randint

from classes.geometry import *

width = 1980
hight = 1080

img = Image.new('RGB', (width, hight), color = (230, 235, 255))

draw = ImageDraw.Draw(img)

n = 40

dots = []

for i in range(n):
    x = randint(0, width)
    y = randint(0, hight)
    dots.append({
        'x': x,
        'y': y,
        'links': [],
        'cnt': 0
    })

for i in dots:
    draw.point((i['x'], i['y']), 'black')    

max_node_pow = 4

for i in range(len(dots)):
    while (dots[i]['cnt'] < max_node_pow):
        for j in range(i+1, len(dots)):
            if (dots[j]['cnt'] > max_node_pow or dots[i]['cnt'] > max_node_pow):
                continue
            if (randint(1, 1) == 1 and geometry.distance(dots[i]['x'], dots[i]['y'], dots[j]['x'], dots[j]['y']) <= randint(500, 800)):
                draw.line((dots[i]['x'], dots[i]['y'], dots[j]['x'], dots[j]['y']), fill=1)
                dots[i]['cnt'] += 1
                dots[j]['cnt'] += 1
        dots[i]['cnt'] += 1
img.save('./images/img3.png')