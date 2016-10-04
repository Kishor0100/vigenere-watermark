import math
from PIL import Image

def psnr(img_a, img_b):
    if img_a.size != img_b.size:
        raise Exception("image size must be equal")

    rms = math.sqrt(mse(img_a, img_b))
    return 20 * math.log10(255 / rms)

def mse(img_a, img_b):
    img_int_a = img_int(img_a.copy().convert("RGB"))
    img_int_b = img_int(img_b.copy().convert("RGB"))
    tmp = sum((sum(a)-sum(b))**2 for a, b in zip(img_int_a, img_int_b))
    return tmp / img_a.width / img_a.height / 3

def img_int(img):
    px = img.load()
    for x in range(img.width):
        for y in range(img.height):
            yield px[x,y]
