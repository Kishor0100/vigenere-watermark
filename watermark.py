import random
from PIL import Image

def insert(filepath, watermarkpath, key, outputpath):
    image = Image.open(filepath)
    watermark = Image.open(watermarkpath).convert("1")
    px_image = image.load()
    px_watermark = watermark.load()

    random.seed(key)
    x_sequence = random.sample(range(image.width), image.width)
    y_sequence = random.sample(range(image.height), image.height)

    for i, x in enumerate(x_sequence):
        for j, y in enumerate(y_sequence):
            p = list(px_image[x,y])
            w = px_watermark[i%watermark.width, j%watermark.height]
            if w: p[0] |= 0b00000001
            else: p[0] &= 0b11111110
            px_image[x,y] = tuple(p)
    image.save(outputpath)

def extract(filepath, key, outputpath):
    image = Image.open(filepath)
    watermark = Image.new("1", image.size)
    px_image = image.load()
    px_watermark = watermark.load()

    random.seed(key)
    x_sequence = random.sample(range(image.width), image.width)
    y_sequence = random.sample(range(image.height), image.height)

    for i, x in enumerate(x_sequence):
        for j, y in enumerate(y_sequence):
            p = px_image[x,y]
            w = (p[0] & 1) * 255
            px_watermark[i,j] = w
    watermark.save(outputpath)
