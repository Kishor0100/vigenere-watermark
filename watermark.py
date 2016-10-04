import random
from PIL import Image

import vigenere

def insert(filepath, watermarkpath, key, outputpath):
    image = Image.open(filepath)
    watermark = Image.new("1", image.size)
    watermark_bin = Image.open(watermarkpath).convert("1")

    px_image = image.load()
    px_watermark_bin = watermark_bin.load()
    px_watermark = watermark.load()
    for x in range(image.width):
        for y in range(image.height):
            px_watermark[x,y] = px_watermark_bin[x%watermark_bin.width, y%watermark_bin.height]
    watermark = vigenere.encrypt_image(watermark, key)
    px_watermark = watermark.load()    

    random.seed(key)
    x_sequence = random.sample(range(image.width), image.width)
    y_sequence = random.sample(range(image.height), image.height)

    for i, x in enumerate(x_sequence):
        for j, y in enumerate(y_sequence):
            p = list(px_image[x,y])
            w = px_watermark[i,j]
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
    vigenere.decrypt_image(watermark, key).save(outputpath)    
